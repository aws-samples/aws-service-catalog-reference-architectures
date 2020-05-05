# AWS Service Catalog Bulk Deployer

This reference architecture creates a framework of lambdas, Step functions, and Service Catalog products which demonstrate how to provision and track many Service Catalog Products.

## Bulk Deployment for Amazon WorkSpaces

<img src=images/wait.jpeg width=90>

### Prerequisites

There are several prerequisites you will need to deploy Amazon WorkSpaces in bulk.

** Note ** You can get this information if you use the Amazon WorkSpace Console to create 1 test WorkSpace instance.

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

  The KMS information is located in the Amazon KMS console (copy the ARN)
  <img src=images/kms.png>

Once you have the information needed your CSV file should look like this.

```
DirectoryId,UserName,BundleId,KMSKey
d-YourDirectoryId,scwpuser001,wsb-8vbljg4r6,arn:aws:kms:us-east-1:676575380427:key/9c631fc8-6b-YOUR-KEY-84a06dfd3
d-YourDirectoryId,scwpuser002,wsb-8vbljg4r6,arn:aws:kms:us-east-1:676575380427:key/9c631fc8-6b-YOUR-KEY-84a06dfd3
```

- Upload the file to an Amazon S3 bucket in your account
- Make note of the bucket name and the key of your file



### Install  
Launch the stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-BulkDeployer-Master&templateURL=https://aws-service-catalog-reference-architectures.s3.amazonaws.com/bulkprovision/bulkmonitor-master-template.json)
