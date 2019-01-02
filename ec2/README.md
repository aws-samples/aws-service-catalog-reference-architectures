# AWS Service Catalog EC2 Reference architecture

When implemented this reference architecture creates an AWS Service Catalog Portfolio called "Service Catalog EC2 Reference Architecture" 
 with associated products. The AWS Service Catalog Product references cloudformation templates for the Amazon EC2 Linux and 
 Windows instances which can be lauched by end users through AWS Service Catalog.  The AWS Service Catalog EC2 product creates 
 either an Aamzon Linux or Microsoft Windows EC2 instance in the VPC and Subnets selected by the end user.
 A Amazon Simple Systems Manager patch baseline, maintenance window and task are created to allow for automated patching of the 
 Aamzon Linux and Microsoft Windows operating systems. The Portfolio also includes a Linux webserver Product with either Apache or NGINX versions.

 
### Install  
1. Launch the IAM group and policy stack for end user provisioning:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-IAM-Endusers&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/iam/sc-enduser-iam.yml)  

2. Launch the EC2 portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-EC2Portfolio&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/ec2/sc-portfolio-ec2.json)  
  * If you have already run the VPC template, then you will put the _output.LaunchRoleName_ from the completed LaunchConstraintRole stack in the _LaunchRoleName_ field (default is SCEC2LaunchRole).  

  
### Install from your own S3 bucket  
1. clone this git repo:  
  ```git clone git@github.com:aws-samples/aws-service-catalog-reference-architectures.git```  
2. Copy everything in the repo to an S3 bucket:  
  ```cd aws-service-catalog-reference-architectures```  
  ```aws s3 cp . s3://[YOUR-BUCKET-NAME-HERE] --exclude "*" --include "*.json" --include "*.yml" --recursive```  
3. In the AWS [CloudFormation console](https://console.aws.amazon.com/cloudformation) choose "Create Stack" and supply the Portfolio S3 url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/ec2/sc-portfolio-ec2.json```  
4. If this is the first portfolio you are creating, then leave _LaunchRoleName_ blank to allow CloudFormation to create the launchconstraint role for you.  
    * If you have already run the VPC template, then you will put the _output.LaunchRoleName_ from the completed LaunchConstraintRole stack in the _LaunchRoleName_ field (default is SCEC2LaunchRole).  
5. Set the _LinkedRole1_ parameter to your _SCProvisioningRole_ name if applicable.
6. Set the "RepoRootURL" parameter to your bucket's root url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/```  
  

### EC2 Architecture with Amazon Linux and Microsoft Windows instances

![sc-ec2-ra-architecture.png](sc-ec2-ra-architecture.png)


