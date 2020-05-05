# AWS Service Catalog Bulk Deployer

This reference architecture creates a framework of lambdas, Step functions, and Service Catalog products which demonstrate how to provision and track many Service Catalog Products.

## Bulk Deployment for Amazon WorkSpaces

<img src=images/wait.jpeg width=90>

### Prerequisites

There are several prerequisites you will need to deploy Amazon WorkSpaces in bulk.

You have to create a comma seprated value file (CSV) with this format:

```
DirectoryId,UserName,BundleId,KMSKey
```
The values contains:

- The Amazon WorkSpaces Drirectory to use
- A set of Amazon WorkSpaces Directory users
- The Amazon WorkSpaces Bundlel id to use
- An Amazon KMS key for encryption

The WorkSpace information is located in the Amazon WorkSpaces console
<img src=images/workspacescreen.png>

The KMS information is located in the Amazon KMS console
<img src=images/kms.png>




### Install  
Launch the stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-BulkDeployer-Master&templateURL=https://aws-service-catalog-reference-architectures.s3.amazonaws.com/bulkprovision/bulkmonitor-master-template.json)
