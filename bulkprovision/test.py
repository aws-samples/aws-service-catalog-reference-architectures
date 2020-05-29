#! /usr/bin/python3
import time
import json
import boto3
from lambda_function import provision_handler,uploadcsv_handler,terminate_handler,monitor_handler,failure_handler,cleanup_handler
import logging
logging.basicConfig()
logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)


######################  SET VALUES HERE FOR YOUR ACCOUNT ##########################
DEFAULT_REGION = 'us-east-1'
CSV_BUCKET= "xxxxxxxxxxx" 
CSV_KEY= "xxxxxxxxxxx" 
DYANMO_TABLE = "xxxxxxxxxxx"
PRODUCT_ID= "prod-xxxxxxxxxxx" # #Bulk deploy product             
PROVISIONINGA_ART_ID="pa-xxxxxxxxxxx" # Workspace
#PROVISIONINGA_ART_ID="pa-xxxxxxxxxxx" #S3 bucket
SC_TEMPLATE_PARAMETER_NAMES = "DirectoryId,UserName,BundleId,KMSKey"
RETRY=2


print(boto3.client('sts').get_caller_identity())


def uploadExec():
    uploadcsv_handler({"csvbucket":CSV_BUCKET,"csvkey":CSV_KEY,"dytable":DYANMO_TABLE, "region":DEFAULT_REGION},None)

def terminate():
    terminate_handler({"status":"AVAILABLE","dytable":DYANMO_TABLE, "region":DEFAULT_REGION},None)

def monitor():
    count = 1
    
    while count > 0:
        count = 0
        cleanup_handler({"status":["FAILED","TERMINATED"],"dytable":DYANMO_TABLE, "region":DEFAULT_REGION}, None)

        # uncomment the line below to override the SSM parameter values for product and provisioning artifact IDs
        provision_handler({"dytable":DYANMO_TABLE, "region":DEFAULT_REGION,
        #"scproductid":PRODUCT_ID,"scpaid":PROVISIONINGA_ART_ID,
        "scparams":SC_TEMPLATE_PARAMETER_NAMES, 
        "tags":[ {"Key":"auto_provision","Value":"SUCCESS"}] } ,None)
        
        resp= monitor_handler({"dytable":DYANMO_TABLE,"status":["PROVISIONING","TERMINATING"], "region":DEFAULT_REGION },None)
        count += resp["statusCount"]
        resp= failure_handler({"dytable":DYANMO_TABLE,"status":["TERMINATING-FAILURE","STATUS-ERROR","PRODUCT-ERROR","PROVISION-ERROR"],"retrythreshold":RETRY, "region":DEFAULT_REGION },None)
        count += resp["statusCount"]
        
        print("waiting...")
        time.sleep(15)
    # endwhile
        
    

if __name__ == "__main__":    
    # comment out lines here to prevent multiple CSV uploads and termination
    uploadExec()
    monitor()    
    #terminate()