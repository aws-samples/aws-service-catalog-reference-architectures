import os
import json
import boto3
import logging
import time
logger = logging.getLogger()

#Ken Walsh 4-20-2020
#Reporting
s3client  = boto3.client('s3')
dyclient = boto3.client('dynamodb')
ses_client =   boto3.client('ses')

def lambda_handler(event,context):
    _beg =  "<html><head><title>Servic Catalog Bulk Deployment for   </title>"  
    _beg += "<link rel=stylesheet href=https://s3.amazonaws.com/kenwalshtestad/cfn/public/css/styletable.css>"
    _beg += "</head><body>"
    _beg += "<table id=customers border=2>"
    localtime = time.asctime( time.localtime(time.time()) )
    _th='<tr><th colspan=4>%s</th></tr><tr>' % localtime
    _r=''
    _th  += '<th>Status</th>' 
    _th  += '<th>BatchId</th>' 
    _th  += '<th>User</th>'  
    _th  += '<th>SC Status</th>'  
    ##########
    
    tablename = os.environ['DynamoTablename']
    sresults = dyclient.scan(TableName=tablename)            
    if 'Items' in sresults:
        for t in sresults['Items']: 
            _r  += '<td>%s</td>' % t['status']['S']
            _r  += '<td>%s</td>' % t['launchparams']['M']['BatchId']['S'] if "BatchId" in t['launchparams']['M'] else "NONE"
            _r  += '<td>%s</td>' % t['launchparams']['M']['UserName']['S']
            _r  += '<td>%s</td></tr><tr>' % t['scproductdetails']['M']['Status']['S']
        _ret = _beg +  '<tr>'+_th +'</tr>\n<tr>'+ _r +'</tr></table>'
        #======================
        m_event ={}
        m_event['etoemail'] = event['ReportEmail']
        m_event['esubject'] = 'sc work spaces bulk deployment'
        DestBucket= os.environ['LambdaZipsBucket']
        _skey = 'content/out/report.html' 
        b_putpriv(DestBucket,_skey,_ret,"text/html")
        _l = gen_surl(DestBucket,_skey)
        m_event['ebody'] = _ret +'<br><a href="' + _l +'">Click me Report</a>'

        if check_for_ses_email(m_event) == True:
             logger.info(sendemail(m_event))
        
        event['EmailInfo'] = m_event
    return  event
##########################
###S3 unctions #############################
def gen_surl(bucketname,keyname):
    url = s3client.generate_presigned_url(ClientMethod='get_object',Params={'Bucket': bucketname,'Key': keyname})
    return url 
def b_putpriv(bucket,key,body,ctype):
  srep = s3client.put_object( ACL='private',Body=body,Bucket=bucket,Key=key, ContentType=ctype,)
  logger.info(srep)
  return srep 
###SES functions############################
def check_for_ses_email(event):    
    emails =   ses_client.list_verified_email_addresses()
    _ret = False
    #logger.info(emails)
    if event['etoemail'] in emails['VerifiedEmailAddresses']:
        logger.info('Found ' +  event['etoemail'] )
        _ret = True
    else:
        response = ses_client.verify_email_identity(EmailAddress= event['etoemail'])
        logger.info('Email address not Found ' +  event['etoemail'] +" Verification sent")        
    return _ret
def sendemail(event):
    charset = "UTF-8"    
    try:
        #Provide the contents of the email.
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [
                    event['etoemail'],
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': charset,
                        'Data': event['ebody'],
                    },
                    'Text': {
                        'Charset': charset,
                        'Data': event['ebody'],
                    },
                },
                'Subject': {
                    'Charset': charset,
                    'Data': event['esubject'],
                },
            },
            Source=event['etoemail'],
        )
    except Exception as e:
      logger.exception(e)
      return(e)   
    else:
      return('EmailSent to ' + event['etoemail'])
      
