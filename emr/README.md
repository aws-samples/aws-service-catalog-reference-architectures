# AWS Service Catalog EMR Reference architecture

This reference architecture creates an AWS Service Catalog Portfolio called 
 "Service Catalog EMR Reference Architecture" with one associated product.
 The AWS Service Catalog Product references a cloudformation template for the
 Amazon EMR cluster which can be lauched by end users through AWS Service Catalog.
 The AWS Service Catalog EMR product creates an Aamzon Elastic MapReduce cluster in the VPC and Subnets
 selected by the end user.  A remote access security group is also created to allow for a bastion host
 to connect to the instances used by EMR via SSH.

### Install  
Launch the EMR portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-EMRPortfolio&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/emr/sc-portfolio-emr.json)


### Install from your own S3 bucket  
1. clone this git repo:  
  ```git clone git@github.com:aws-samples/aws-service-catalog-reference-architectures.git```  
2. Copy everything in the repo to an S3 bucket:  
  ```cd aws-service-catalog-reference-architectures```  
  ```aws s3 cp . s3://[YOUR-BUCKET-NAME-HERE] --exclude "*" --include "*.json" --include "*.yml" --recursive```  
3. In the AWS [CloudFormation console](https://console.aws.amazon.com/cloudformation) choose "Create Stack" and supply the Portfolio S3 url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/emr/sc-portfolio-emr.json```  
4. Set the _LinkedRole1_ parameter to your _SCProvisioningRole_ name if applicable.
5. Change the "RepoRootURL" parameter to your bucket's root url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/```


### Amazon Elastic MapReduce Cluster

![sc-emr-ra-architecture.png](sc-emr-ra-architecture.png)

