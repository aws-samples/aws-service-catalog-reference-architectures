import uuid
import json
import logging
from botocore.exceptions import ClientError
from common import aws_clients
logger = logging.getLogger()

class SC_Provision(aws_clients):
    def __init__(self, event):
        super().__init__(event)
    
    def UploadCSV(self):
        '''
        uploads data from the given csv to dynamo with an initial status of NEW
        '''
        # get the csv file
        csv_bucket = self.get_config_value("csvbucket")
        csv_key = self.get_config_value("csvkey")        
        BatchId = self.get_config_value("BatchId")
        input_dict = self.s3_get_csvasdict(csv_bucket, csv_key)    
        
        # build the dynamo object
        arr = [ ]
        for item in input_dict:
            if BatchId is not None:
                item["BatchId"] = BatchId
            obj={
                "guidkey": str(uuid.uuid4()),
                "status": "NEW" ,                
                "launchparams": item
            }
            arr.append(obj)
        count = len(arr)
        # upload this to the dynamo table
        self.dynamo_write_batch(arr)
        logger.info("Loaded {} new entries to {}".format(count, self.getDynamoTableName()))
        return(self.generate_return(count))

    def TerminateProducts(self):
        '''
        Terminates entries with the incmoing status 
        '''
        qry_status = self.get_config_value("status")
        new_items = self.dynamo_query("status",qry_status)
        logger.info("Found {} items to Terminate with status {}".format(len(new_items), qry_status))
        #track success and failure
        count = 0
        errors = 0
        for drow in new_items:
            # setup variables to use later
            failed = False
            errordetails = None
            # keep the error message if we have one
            if "errordetails" in drow:
                errordetails = drow["errordetails"]                
            dbstatus = "TERMINATING"
            ppid= drow["scproductdetails"]["ProvisionedProductId"]
            param_dict = drow["launchparams"]
            guidkey = drow["guidkey"]            
            ppdetails = {
                'ProvisionedProductId':ppid,
                'RecordId':drow["scproductdetails"]['RecordId'],
                'CreatedTime':str(drow["scproductdetails"]['CreatedTime']),
                'Status':drow["scproductdetails"]['Status']
            }
            
            try:
                # terminate the product and record the important parts of the response
                resp = self.sc_terminate_product(ppid)
                ppdetails['RecordId']=resp['RecordDetail']['RecordId']
                ppdetails['Status'] = resp['RecordDetail']['Status']                    
            except ClientError as ce:
                msg = ce.response['Error']['Message']
                if msg.startswith("Provisioned product not found: "):
                    #This was a good status termination, lets mark it and we're done with it now.
                    dbstatus = "TERMINATED"
                    ppdetails["Status"] = "TERMINATED" 
                    count += 1
                else:
                    # something wrong from the API call. this is where you will see the CFn Errors
                    logger.error("ClientError: {}".format(msg))    
                    errordetails = ce.response['Error']
                    failed = True
            except Exception as e:
                # Something else wrong?
                logger.error(e)                
                failed = True
            else:
                count += 1
                                    
            if failed:
                errors += 1
                dbstatus = "TERMINATION-ERROR"
            
            #update the dynamo table
            self.updateItem(guidkey,drow["status"],dbstatus, param_dict, ppdetails, errordetails)
        if len(new_items) > 0:
            logger.info("Terminated {} of {} products with {} errors using status:{}".format(count, len(new_items), errors, qry_status))
        return(self.generate_return(count))
        
    def ProvisionProducts(self):
        '''
        This will go through the Dynamo table from the config and provision the given product using the params from matching the incoming scparams list.
        '''
        # config overides SSM
        sc_param_keys = self.get_config_value("scparams").split(',')
        sc_productid = self.get_config_value("scproductid")
        sc_paid = self.get_config_value("scpaid")
        provision_threshold = self.get_config_value("provision_threshold")
        if provision_threshold is None:
            provision_threshold = 10
        
        # try to get them from SSM
        if sc_productid is None:
            sc_productid = self.ssm_get_parameter("/bulkdeploy/productid")
        if sc_paid is None:
            arr = self.ssm_get_parameter("/bulkdeploy/provisioningid").split('|')
            # grab the first if there are many
            sc_paid = arr[0]
        
        # get new items        
        new_items = self.dynamo_query_multi("status",["NEW","RETRY"])
        logger.info("Found {} new items to provision".format(len(new_items)))
        count = 0
        errors = 0
        for drow in new_items[:provision_threshold]:
            # setup variables to use later
            arr_params = []
            guidkey = drow["guidkey"]                                                    
            param_dict = drow["launchparams"]
            failed = False
            ppdetails = None
            errordetails = None
            dbstatus = "PROVISIONING"
            # keep the error message if we have one
            if "errordetails" in drow:
                errordetails = drow["errordetails"]
            
            try:
                # Map the incoming launchparams from the dynamo entry to the launch params from our event config
                for paramkey in sc_param_keys:
                    par_obj = { "Key":paramkey,"Value":param_dict[paramkey] }
                    arr_params.append(par_obj)               
                
                # provision the product and record the important parts of the response
                resp = self.sc_provision_product(sc_productid, sc_paid, guidkey, arr_params)
                ppdetails = {
                    'ProvisionedProductId':resp['RecordDetail']['ProvisionedProductId'],
                    'RecordId':resp['RecordDetail']['RecordId'],
                    'CreatedTime':str(resp['RecordDetail']['CreatedTime']),
                    'Status': resp['RecordDetail']['Status']
                }
            except ClientError as ce:
                # something wrong from the API call. this is where you will see the CFn Errors
                msg = ce.response['Error']['Message']
                logger.error("ClientError: {}".format(msg))
                if ce.response['Error']['Code'] == "InvalidParametersException" and msg == "A stack named {} already exists.".format(guidkey):
                    # we got a duplicate???  just fail it, no need to retry
                    errors += 1
                    dbstatus = "DUPLICATE"
                else:
                    errordetails = ce.response['Error']
                    failed = True            
            except  KeyError as ke:
                msg = "PROVISION-ERROR: Keys from CSV do not match template! Could not find {}".format(ke)
                logger.error(msg)
                errordetails = msg
                failed = True            
            except Exception as e:
                # Something else wrong?
                logger.error(e)                                
                failed = True
            else:
                count += 1
            
            # mark the status according to the outcome from above            
            if failed:
                errors += 1
                dbstatus = "PROVISION-ERROR"
                
            #update the dynamo table
            self.updateItem(guidkey,drow["status"],dbstatus, param_dict, ppdetails, errordetails)            
                    
        if len(new_items) > 0:
            logger.info("Provisioned {} of {} new products with {} errors using ProductID:{} PAID:{}".format(count, len(new_items), errors, sc_productid, sc_paid))
        return(self.generate_return(count))
       

