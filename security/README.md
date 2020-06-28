# AWS Service Catalog GuardDuty Reference architecture

This reference architecture creates an AWS Service Catalog Portfolio called 
 "Service Catalog - AWS GuardDuty Reference Architecture" with one associated product.
 The AWS Service Catalog Product references a cloudformation template for the
 a GuardDuty which can be launched by end users through AWS Service Catalog.
 The AWS Service Catalog GuardDuty product enables GuardDuty Delegated Aministrator account in all AWS Regions. GuardDuty findings across all regions are exported to aws-controltower-guardduty-[account id]-[region] bucket in the the Control Tower Log Archive account.

### Install  
Launch the GuardDuty portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-GuardDuty-Portfolio&templateURL=https://aws-service-catalog-reference-architectures.s3.amazonaws.com/security/sc-portfolio-gd.json)


### Install from your own S3 bucket  
1. clone this git repo:  
  ```git clone git@github.com:aws-samples/aws-service-catalog-reference-architectures.git```  
2. Copy everything in the repo to an S3 bucket:  
  ```cd aws-service-catalog-reference-architectures```  
  ```aws s3 cp . s3://[YOUR-BUCKET-NAME-HERE] --exclude "*" --include "*.json" --include "*.yml" --recursive```  
3. In the AWS [CloudFormation console](https://console.aws.amazon.com/cloudformation) choose "Create Stack" and supply the Portfolio S3 url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/security/sc-portfolio-gd.json```  
5. Set the _LinkedRole1_ and _LinkedRole2_ parameters to any additional end user roles you may want to link to the Portfolio.
6. Set the _CreateEndUsers_ parameter to No if you have already run a Portfolio stack from this repo (ServiceCatalogEndusers already exists).
7. Change the _RepoRootURL_ parameter to your bucket's root url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/``` 

