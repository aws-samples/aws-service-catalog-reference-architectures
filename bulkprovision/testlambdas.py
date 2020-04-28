#! /usr/bin/python3
import time
import json
import boto3
from lambda_function import provision_handler,uploadcsv_handler,terminate_handler,monitor_handler,failure_handler
import logging
logging.basicConfig()
logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)

######################  SET VALUES HERE FOR YOUR ACCOUNT ##########################
DEFAULT_REGION = 'us-east-1'
CSV_BUCKET= "xxxxxxxxxxx" 
CSV_KEY= "xxxxxxxxxxx" 
PRODUCT_ID= "prod-xxxxxxxxxxx" # #Bulk deploy product             
PROVISIONINGA_ART_ID="pa-xxxxxxxxxxx" # Workspace
#PROVISIONINGA_ART_ID="pa-xxxxxxxxxxx" #S3 bucket
SC_TEMPLATE_PARAMETER_NAMES = "DirectoryId,UserName,BundleId,KMSKey"
RETRY=2

#using session profile???
#session = boto3.Session(profile_name='')
#lambdaclient = session.client('lambda', DEFAULT_REGION)

#using temporary credentials??
lambdaclient = boto3.client('lambda', DEFAULT_REGION)

def doLambda(functionname,params):
    payload = json.dumps(params).encode('utf-8')
    resp = lambdaclient.invoke(
        FunctionName=functionname,
        InvocationType="Event",
        Payload=payload
    )
    print(resp)

def uploadCSV():        
    # load the CSV file
    doLambda("SC-BULK-CSV-DYNAMO", {"csvbucket":CSV_BUCKET,"csvkey":CSV_KEY})    
    time.sleep(5)

def lambdaLoops():
    count = 10
    while count > 0:
        
        # uncomment the lines below to override the SSM parameter values for product and provisioning artifact IDs
        prov_payload = {
            "scparams":SC_TEMPLATE_PARAMETER_NAMES,
            #"scproductid":PRODUCT_ID,
            #"scpaid":PROVISIONINGA_ART_ID,
            "tags":[ {"Key":"auto_provision","Value":"SUCCESS"}] 
        }        
        resp = doLambda("SC-BULK-PROVISION", prov_payload)        
        
        # kick off the SC-BULK-MONITOR function for each of the following status flags.
        obj = {"status":["PROVISIONING", "TERMINATING"]}
        func = "SC-BULK-MONITOR"
        resp = doLambda(func, obj)
            
        # TERMINATING-FAILURE and error status flags use the SC-BULK-HANDLE-FAILED function and the retry threshold value
        status_flags = ["TERMINATING-FAILURE","STATUS-ERROR","PRODUCT-ERROR","PROVISION-ERROR"]
        obj = {"status":status_flags,"retrythreshold":RETRY }
        func = "SC-BULK-HANDLE-FAILED"
        resp = doLambda(func, obj)
        
        doLambda("SC-BULK-CLEANUP",{"status":["TERMINATED"] })
        
        count -= 1
        print("waiting...")
        time.sleep(15)

def Lambdaterminate():
    doLambda("SC-BULK-TERMINATE",{"status":"AVAILABLE"})

if __name__ == "__main__":
    # comment out lines here to prevent multiple CSV uploads and termination
    #Lambdaterminate()
    uploadCSV()
    lambdaLoops()
    