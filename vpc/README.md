# AWS Service Catalog VPC Reference architecture

This reference architecture creates an AWS Service Catalog Portfolio called "Service Catalog VPC Reference Architecture". 
 The AWS Service Catalog Products reference cloudformation templates for the Amazon VPC which can be lauched by end users through 
 AWS Service Catalog.  The product creates a VPC with two public and private subnets across two availability zones.  
 The VPC includes an Internet Gateway and a managed NAT Gateway in each public subnet as well as VPC Route Tables and 
 Network ACLs that allow for communication between the public and private subnets.  Optionally, an Amazon Linux bastion instance 
 and a Security Group can be deployed into the public subnet to allow for remote connectivity to the bastion instance.

 
### Install  
Launch the VPC portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-VPCPortfolio&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/vpc/sc-portfolio-vpc.json)
    * If you have already run the EC2 template, then you will put the _output.LaunchRoleName_ from the completed LaunchConstraintRole stack in the _LaunchRoleName_ field (default is SCEC2LaunchRole).  

  
### Install from your own S3 bucket  
1. clone this git repo:  
  ```git clone git@github.com:aws-samples/aws-service-catalog-reference-architectures.git```  
2. Copy everything in the repo to an S3 bucket:  
  ```cd aws-service-catalog-reference-architectures```  
  ```aws s3 cp . s3://[YOUR-BUCKET-NAME-HERE] --exclude "*" --include "*.json" --include "*.yml" --recursive```  
3. In the AWS [CloudFormation console](https://console.aws.amazon.com/cloudformation) choose "Create Stack" and supply the Portfolio S3 url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/vpc/sc-portfolio-vpc.json```  
4. If this is the first portfolio you are creating, then leave _LaunchRoleName_ blank to allow CloudFormation to create the launchconstraint role for you.  
    * If you have already the EC2 template, then you will put the _output.LaunchRoleName_ from the completed LaunchConstraintRole stack in the _LaunchRoleName_ field (default is SCEC2LaunchRole).  
5. Set the _LinkedRole1_ and _LinkedRole2_ parameters to any additional end user roles you may want to link to the Portfolio.
6. Set the _CreateEndUsers_ parameter to No if you have already run a Portfolio stack from this repo (ServiceCatalogEndusers already exists).
7. Change the _RepoRootURL_ parameter to your bucket's root url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/``` 

### Multi-Availability Zone Architecture with Amazon Linux Bastion Instance

![sc-vpc-ra-architecture-multi-az.png](sc-vpc-ra-architecture-multi-az.png)
