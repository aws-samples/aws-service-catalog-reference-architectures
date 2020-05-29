import logging
from bulkexecute import SC_Provision
from bulkmonitor import SC_Monitor

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def uploadcsv_handler(event, context):
    logger.debug(event)
    provisioner = SC_Provision(event)
    return(provisioner.UploadCSV())    

def provision_handler(event, context):
    logger.debug(event)
    provisioner = SC_Provision(event)
    return(provisioner.ProvisionProducts())

def terminate_handler(event, context):
    logger.debug(event)
    provisioner = SC_Provision(event)
    return(provisioner.TerminateProducts())

def failure_handler(event, context):
    logger.debug(event)
    monitor = SC_Monitor(event)
    return(monitor.HandleFailed())

def monitor_handler(event, context):
    logger.debug(event)
    monitor = SC_Monitor(event)
    return(monitor.Run())    
 
def cleanup_handler(event, context):
    logger.debug(event)
    monitor = SC_Monitor(event)
    return(monitor.RemoveEntries())
 
 