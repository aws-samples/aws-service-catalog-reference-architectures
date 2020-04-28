import json
import logging
from botocore.exceptions import ClientError
from common import aws_clients
logger = logging.getLogger()

class SC_Monitor(aws_clients):
    def __init__(self, event):
        super().__init__(event)
        self._status = self.get_config_value("status")
        self._retries = self.get_config_value("retrythreshold")
        if self._retries is None:
            self._retries = 5
    
    def HandleFailed(self):
        '''
        Handles failed status flags and retry logic.  Entries will either be retried or end up FAILED
        '''
        # get the provisioning products and poll them for updates
        prov_items = self.dynamo_query("status",self._status)
        logger.info("Found {} items to Recover with status {}".format(len(prov_items), self._status))
        count = 0
        errors = 0
        for drow in prov_items:
            
            # grab some initial values to be used later
            failed = False
            errordetails = None
            retry=False
            ppdetails = None
            # keep the error message if we have one
            if "errordetails" in drow:
                errordetails = drow["errordetails"]
            dbstatus = drow["status"] # this is the status key from dynamo - status used for this program to track    
            param_dict = drow["launchparams"]
            guidkey = drow["guidkey"]
            
            #do we even have a product or did it fail before launcnh?
            if drow["scproductdetails"] is None:
                # product totatally failed, mark it as retry
                retry=True
            else:
                #continuing, if we have product details we can build the ppdetails object for later use
                ppid= drow["scproductdetails"]["ProvisionedProductId"]   
                ppdetails = {
                    'ProvisionedProductId':ppid,
                    'RecordId':drow["scproductdetails"]['RecordId'],
                    'CreatedTime':str(drow["scproductdetails"]['CreatedTime']),
                    'Status':drow["scproductdetails"]['Status']
                }
                
                try:
                    # get the product then record the important parts of the response
                    resp = self.sc_describe_prov_product(ppid)
                    prod_status = resp['ProvisionedProductDetail']['Status']  # this is the status from SC we use this to set our own dbstatus value
                    ppdetails['RecordId']=resp['ProvisionedProductDetail']['LastRecordId']
                    ppdetails['Status'] = prod_status    
                    
                    # handle the status messages 
                    if prod_status == 'AVAILABLE':
                        dbstatus = "AVAILABLE"
                    elif prod_status in ['TAINTED','ERROR']:
                        if dbstatus in ["PROVISIONING","STATUS-ERROR","PRODUCT-ERROR"]:
                            # We are here becuase the product was marked as provisioning by us, but SC returned an error
                            # if it failed to provision, lets terminate it in Service Catalog
                            resp = self.sc_terminate_product(ppid)
                            failed = True
                        else:
                            # failed at some other point - failed termination??
                            errors += 1
                            dbstatus = "PRODUCT-ERROR"
                    else:
                        # something else is wrong - lets just terminate
                        resp = self.sc_terminate_product(ppid)
                        failed = True
                        
                except ClientError as ce:
                    msg = ce.response['Error']['Message']
                    # tried to find the product details, but it is gone. So we asked it to be terminated and that has now happened
                    if msg.startswith("Provisioned product not found: "):
                        # instead of marking it terminated like normal, we mark it RETRY and let the provisioner run it again                    
                        retry = True
                    elif msg.startswith("Can't terminate provisioned product because it's still under change or its status does not allow further operation"):
                        # its in a terminating state??  just wait on this one
                        # leave the orginal error in place
                        failed = True
                    else:
                        # something wrong from the API call. this is where you will see the Errors returned from SC
                        errordetails =ce.response['Error']                        
                        logger.error("ClientError: {}".format(msg))
                        failed = True
                except Exception as e:
                    # Something else wrong?
                    logger.error(e)
                    failed = True
                else:
                    count += 1
                
            if not 'retries' in param_dict:
                param_dict['retries'] = 0
                
            if retry:                
                # instead of marking it terminated like normal, we mark it RETRY and let the provisioner run it again
                param_dict['retries'] = param_dict['retries'] + 1
                if param_dict['retries'] < self._retries:
                    dbstatus = "RETRY"
                    count += 1
                else:
                    # this is our final stop, we retried and could not proceed any further
                    logger.error("Provision failed for {} after {} tries, giving up. Error Message:{}".format(guidkey, param_dict['retries'], errordetails))
                    errors += 1
                    dbstatus = "FAILED"
            
            if failed:
                errors += 1
                if param_dict['retries'] < self._retries:
                    logger.error("Provision failed for {} after {} tries, giving up. Error Message:{}".format(guidkey, param_dict['retries'], errordetails))
                    dbstatus = "FAILED"
                else:
                    dbstatus = "TERMINATING-FAILURE"
            
            #update the dynamo table
            self.updateItem(guidkey,drow["status"],dbstatus, param_dict, ppdetails, errordetails)
                    
        if len(prov_items) > 0:
            logger.info("Recovered {} of {} products with {} errors using status:{}".format(count, len(prov_items), errors, self._status))
        return(self.generate_return(count))
    

    def RemoveEntries(self, status_arr=None):
        '''
        the function will clean up entries in Dynamo. use this mainly to remove TERMINATED status entries
        '''
        if status_arr is None:
            status_arr = self._status
        count = 0
        errors = 0
        total = 0
        
        prov_items = self.dynamo_query_multi("status",status_arr)
        total=len(prov_items)
        logger.info("Found {} items to remove with status {}".format(len(prov_items), status_arr))
        failed = False
        for drow in prov_items:
            dbstatus = drow["status"] 
            guidkey = drow["guidkey"]
            try:
                key = {
                    "guidkey": guidkey,
                    "status":  dbstatus
                }  
                self.dynamo_delete_item(key)
            except ClientError as ce:
                msg = ce.response['Error']['Message']
                logger.error("ClientError: {}".format(msg))
                failed = True
            except Exception as e:
                # Something else wrong?
                logger.error(e)
                failed = True
            else:
                count += 1
            
            if failed:
                errors += 1
                    
        if total > 0:
            logger.info("Removed {} of {} entries with {} errors using status:{}".format(count, total, errors, status_arr))
        return(self.generate_return(count))
    
    
    
    def Run(self):
        '''
        Main monitoring process.  This will update status flags based on response from Service Catalog
        '''
        # get the provisioning products and poll them for updates
        prov_items = self.dynamo_query("status",self._status)
        logger.info("Found {} items to Update with status {}".format(len(prov_items), self._status))
        count = 0
        errors = 0
        for drow in prov_items:
            
            ppid= drow["scproductdetails"]["ProvisionedProductId"]   
            dbstatus = drow["status"]
            param_dict = drow["launchparams"]
            guidkey = drow["guidkey"]            
            ppdetails = {
                'ProvisionedProductId':ppid,
                'RecordId':drow["scproductdetails"]['RecordId'],
                'CreatedTime':str(drow["scproductdetails"]['CreatedTime']),
                'Status':drow["scproductdetails"]['Status']
            }            
            failed = False
            errordetails = None
            # keep the error message if we have one
            if "errordetails" in drow:
                errordetails = drow["errordetails"]            
              
            try:
                # update the product and record the important parts of the response
                resp = self.sc_describe_prov_product(ppid)                              
                prod_status = resp['ProvisionedProductDetail']['Status']
                ppdetails['RecordId']=resp['ProvisionedProductDetail']['LastRecordId']
                ppdetails['Status'] = prod_status
                
                # handle the status messages 
                if prod_status == 'AVAILABLE':
                    dbstatus = "AVAILABLE"
                    errordetails = None # if it worked, lets clear out the error message to avoid confusion
                elif prod_status in ['TAINTED','ERROR']:
                    if dbstatus in ["PROVISIONING"]:
                        # if it failed to provision, terminate it in Service Catalog
                        errordetails = resp['ProvisionedProductDetail']['StatusMessage']
                        resp = self.sc_terminate_product(ppid)                        
                        dbstatus = "TERMINATING-FAILURE"
                    else:
                        # failed at some other point - failed termination?? or something else
                        dbstatus = "PRODUCT-ERROR"                    
                elif prod_status in ['UNDER_CHANGE','PLAN_IN_PROGRESS']:
                    # is it terminating?
                    if dbstatus != "TERMINATING":
                        dbstatus = "PROVISIONING"                        
                
            except ClientError as ce:
                msg = ce.response['Error']['Message']
                # tried to find the product details, but it is gone....                
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
                dbstatus = "STATUS-ERROR"
                
            #update the dynamo table
            self.updateItem(guidkey,drow["status"],dbstatus, param_dict, ppdetails, errordetails)
                    
        self.RemoveEntries(["DUPLICATE"])
        if len(prov_items) > 0:
            logger.info("Updated {} of {} products with {} errors using status:{}".format(count, len(prov_items), errors, self._status))        
        return(self.generate_return(count))
    
    
