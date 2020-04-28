import os
import boto3
import botocore
from boto3.dynamodb.conditions import Key, Attr
import csv
import urllib3
import json
import logging

http = urllib3.PoolManager()
logger = logging.getLogger()

ACCOUNT_ID  = boto3.client('sts').get_caller_identity()['Account'] 
DEFAULT_REGION = boto3.session.Session().region_name

def cfnresponse(event, context, responseStatus, responseData={}, physicalResourceId=None, noEcho=False):    
    responseBody = {}
    responseBody['Status'] = responseStatus
    responseBody['Reason'] = 'See the details in CloudWatch Log Stream: ' + context.log_stream_name
    responseBody['PhysicalResourceId'] = physicalResourceId or context.log_stream_name
    responseBody['StackId'] = event['StackId']
    responseBody['RequestId'] = event['RequestId']
    responseBody['LogicalResourceId'] = event['LogicalResourceId']
    responseBody['NoEcho'] = noEcho
    responseBody['Data'] = responseData
    json_responseBody = json.dumps(responseBody)    
    headers = {'content-type' : '','content-length' : str(len(json_responseBody))}
    try:
        response = http.request('PUT',event['ResponseURL'],body=json_responseBody.encode('utf-8'),headers=headers)
        logger.debug('Status code: ' + response.reason)
    except Exception as e:
        logger.error('send(..) failed executing requests.put(..): ' + str(e))

class aws_clients:
    def __init__(self, event):
        self._active_region = DEFAULT_REGION
        self.EVENT_OBJECT = event
        self._ssm_client  = None
        self._sc_client   = None
        self._s3_client   = None
        self._dynamo_table = None 
        self._dynamo_tablename = None       
        if 'DynamoTablename' in os.environ:
            self._dynamo_tablename = os.environ['DynamoTablename']        
        self._load_config()

    def _load_config(self):
        # any config values coming in with the event object?
        if self.get_config_value("region") is not None:
            self._active_region  = self.get_config_value("region")
        
        #setup clients
        self._ssm_client  = boto3.client('ssm',self._active_region)
        self._sc_client   = boto3.client('servicecatalog',self._active_region)
        self._s3_client   = boto3.client('s3',self._active_region)
        
        # setup dynamo resource
        self._dynamodb_rsrc = boto3.resource('dynamodb', region_name=self._active_region)
        if self._dynamo_tablename is None:
            self._dynamo_tablename = self.get_config_value("dytable")
        self._dynamo_table = self._dynamodb_rsrc.Table(self._dynamo_tablename)
        
        logger.debug({"IncomingEvent":self.EVENT_OBJECT})

    def get_config_value(self, key):
        ret = None
        if key in self.EVENT_OBJECT:
            ret = self.EVENT_OBJECT[key]
        elif "ResourceProperties" in self.EVENT_OBJECT and key in self.EVENT_OBJECT["ResourceProperties"]: 
            # coming in from Cloudformation
            ret = self.EVENT_OBJECT["ResourceProperties"][key]
        else:
            logger.info("key {} not found in {}".format(key, self.EVENT_OBJECT))
        return(ret)

    def getDynamoTableName(self):
        return(self._dynamo_tablename)
        
    def get_account_id(self):
        return(ACCOUNT_ID)
        
    def generate_return(self, count):
        self.EVENT_OBJECT["statusCount"] = count 
        return(self.EVENT_OBJECT)

    ###########
    #   S3
    ###########
    def s3_get_csvasdict(self, bucket,key):
        lines = self.s3_get_string(bucket,key).split()
        reader = csv.DictReader(lines)
        return(reader)

    def s3_get_string(self, bucket,key):
        object = self._s3_client.get_object(Bucket=bucket,Key=key)
        return(object['Body'].read().decode('utf-8'))

    def s3_get_json(self, bucket,key):
        str_content = self.s3_get_string(bucket,key)
        json_content = json.loads(str_content)
        return(json_content)
    
    
    #################
    #   dynamoDB
    #################    
    
    def updateItem(self, guidkey, original_status, dbstatus, param_dict, ppdetails, errordetails):
        item = {
            "guidkey": guidkey,
            "status": dbstatus,                
            "launchparams": param_dict,
            "scproductdetails":ppdetails
        }        
        # add the error details if there was an error
        if errordetails is not None:
            item["errordetails"] = errordetails
        
        key = {
                "guidkey": guidkey,
                "status":  original_status
        }              
        # changing a key, so we need to delete and add. use the original status code
        self.dynamo_replace_item(key, item)
    
    def dynamo_replace_item(self, key, newitem):
        del_resp = self.dynamo_delete_item(key)
        logger.debug(del_resp)
        resp = self.dynamo_put_item(newitem)
        logger.debug(resp)
        return(resp)
    
    def dynamo_put_item(self, item):        
        resp = self._dynamo_table.put_item(Item=item)
        logger.debug(resp)
        return(resp)     
    
    def dynamo_write_batch(self, arr_items):        
        with self._dynamo_table.batch_writer() as batch:
            for item in arr_items:
                batch.put_item(Item=item)    
    
    def dynamo_delete_item(self, key):        
        resp = self._dynamo_table.delete_item(
            Key=key
        )
        logger.debug(resp)
        return(resp)        
        
    def dynamo_query(self, key, value):
        if isinstance(value, list):
            # did we get a list for value?  then return the multi query
            return(self.dynamo_query_multi(key,value))
    
        resp = self._dynamo_table.query(
            ConsistentRead= True,
            KeyConditionExpression=Key(key).eq(value)
        )       
        logger.debug(resp)
        return(resp["Items"])

    def dynamo_query_multi(self, key, value_arr):
        '''
        Does a union of multiple queries for a single key and multiple values
        '''
        items = []
        for value in value_arr:
            resp = self._dynamo_table.query(
                ConsistentRead= True,
                KeyConditionExpression=Key(key).eq(value) 
            )   
            logger.debug(resp)
            items += resp["Items"]        
        return(items)

    #########################
    #   SSM Parameter
    #########################      
    
    def ssm_get_parameter(self, param_path):
        resp = self._ssm_client.get_parameter(
            Name=param_path,
            WithDecryption=True
        )
        logger.debug(resp)
        return(resp['Parameter']["Value"])


    #########################
    #   Service Catalog
    #########################      
    def sc_provision_product(self, productid,paid,productname,arr_params):
        arr_tags = self.get_config_value("tags")
        if arr_tags is None:
            arr_tags = []
        resp = self._sc_client.provision_product(ProvisionedProductName=productname, ProductId=productid, ProvisioningArtifactId=paid, ProvisioningParameters=arr_params, Tags=arr_tags )
        logger.debug(resp)
        return(resp)
    
    def sc_describe_prov_product(self, provisionedprodid):
        resp = self._sc_client.describe_provisioned_product(Id=provisionedprodid)
        logger.debug(resp)
        return(resp)
    
    def sc_terminate_product(self, provisionedprodid):
        resp = self._sc_client.terminate_provisioned_product(ProvisionedProductId=provisionedprodid)
        logger.debug(resp)
        return(resp)
    

