# AWS Service Catalog ECS Reference architecture

This reference architecture creates an AWS Service Catalog Portfolio called "Service Catalog Containers Reference Architecture"  
The Portfolio provides 3 products which create a full pipeline from codecommit to container deployment in Fargate.  
First the whole portfolio, then create the cluster and codepipeline products.  Use the provisioned codepipeline product to checkin your code and supply a docker file.
adjust the skeleton builspecs in the codepipeline subfolder to fit your project tests and builds.  Check-in the code to the new codecommit repo. CodePipeline will validate, build, and push the checked in code to ECR.
 Once the container is in ECR you can use the supplied Fargate Task product to create an ECS task definition which can then be launched in the previously provisioned Fargate Cluster.

### Install  
Launch the Container portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/#/stacks/new?stackName=SC-RA-ECS-Portfolio&templateURL=https://aws-service-catalog-reference-architectures.s3.amazonaws.com/ecs/sc-portfolio-ecs.json)


### Install from your own S3 bucket  
1. clone this git repo:  
  ```git clone git@github.com:aws-samples/aws-service-catalog-reference-architectures.git```  
2. Copy everything in the repo to an S3 bucket:  
  ```cd aws-service-catalog-reference-architectures```  
  ```aws s3 cp . s3://[YOUR-BUCKET-NAME-HERE] --exclude "*" --include "*.json" --include "*.yml" --recursive```  
3. In the AWS [CloudFormation console](https://console.aws.amazon.com/cloudformation) choose "Create Stack" and supply the Portfolio S3 url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/glue/sc-portfolio-glue.json```  
5. Set the _LinkedRole1_ and _LinkedRole2_ parameters to any additional end user roles you may want to link to the Portfolio.
6. Set the _CreateEndUsers_ parameter to No if you have already run a Portfolio stack from this repo (ServiceCatalogEndusers already exists).
7. Change the _RepoRootURL_ parameter to your bucket's root url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/``` 

