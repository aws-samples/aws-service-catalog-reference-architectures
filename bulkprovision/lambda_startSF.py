import os
import boto3
import json
import logging
from common import cfnresponse
client = boto3.client('stepfunctions')
logger = logging.getLogger()


def handler(event, context):
  if event['RequestType'] != 'Delete':
    try:
      doupload=True if event['ResourceProperties']['doupload'] == 'True' else False
      input = {
        "doupload":doupload,
        "waitseconds":event['ResourceProperties']['waitseconds'],
        "ReportEmail":event['ResourceProperties']['ReportEmail'],        
        "csv":{ 
            "csvbucket":event['ResourceProperties']['csvbucket'], 
            "csvkey":event['ResourceProperties']['csvkey'],
            "BatchId":event['ResourceProperties']['BatchId']
        },
        "provision": { 
          "scparams":event['ResourceProperties']['scparams'],
          "tags":event['ResourceProperties']['tags']
      }}
      client.start_execution(
        stateMachineArn=os.environ["statemachinearn"],        
        input=json.dumps(input))
    except e:
      logger.exception(e)
      cfnresponse(event, context, 'FAILED', {"error":repr(e)})
      return
  cfnresponse(event, context, 'SUCCESS')