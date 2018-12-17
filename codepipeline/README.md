# AWS Service Catalog CodePipeline Automation Reference blueprint

This reference blueprint demonstrates how an organization can leverage CodePipeline to automate the management and deployment of Serivce Catalog Portfolios, Products, and Resources.

## Getting Started

When implemented this reference blueprint creates an AWS CodeCommit Repo, CodePipeline, and CodeBuild. 
This pipeline will allow 


[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-IACPipeline&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/codepipeline/sc-codepipeline-ra.json)  
(https://s3.amazonaws.com/aws-service-catalog-reference-architectures/codepipeline/sc-codepipeline-ra.json)[https://s3.amazonaws.com/aws-service-catalog-reference-architectures/codepipeline/sc-codepipeline-ra.json]


### Install from your own S3 bucket  
1. clone this git repo:  
  ```git clone git@github.com:aws-samples/aws-service-catalog-reference-architectures.git```  
1. Copy everything in the repo to an S3 bucket:  
  ```cd aws-service-catalog-reference-architectures```  
  ```aws s3 cp . s3://[YOUR-BUCKET-NAME-HERE] --exclude "*" --include "*.json" --include "*.yml" --recursive```  
2. In the AWS [CloudFormation console](https://console.aws.amazon.com/cloudformation) choose "Create Stack" and supply the Portfolio S3 url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/codepipeline/sc-codepipeline-ra.json```  
3. If this is the first portfolio you are creating, then leave _LaunchRoleName_ blank to allow CloudFormation to create the launchconstraint role for you.  
    * If you have already run the VPC template, then you will put the _output.LaunchRoleName_ from the completed LaunchConstraintRole stack in the _LaunchRoleName_ field (default is SCEC2LaunchRole).  
4. Set the _LinkedRole1_ parameter to your _SCProvisioningRole_ name.
5. Set the "RepoRootURL" parameter to your bucket's root url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/```  
  

### CodePipeline which automatically updates ServiceCatalog when templates are checked into CodeCommit  



