# AWS Service Catalog Amazon SageMaker Reference architecture

This reference architecture creates an AWS Service Catalog Portfolio called 
 "Service Catalog - Amazon SageMaker Reference Architecture" with one associated product.
 The AWS Service Catalog Product references a cloudformation template for the
 a Amazon SageMaker which can be launched by end users through AWS Service Catalog.
 The Amazon Sagemaker -Amazon EMR Backed Notebook instance creates an EMR cluster, an Amazon SageMaker notebook instance and connects the two. You will be able to use the template to write pyspark code that executes on the EMR cluster.

### Install  
Launch the Amazon SageMaker portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-Amazon-SageMaker-Portfolio&templateURL=https://aws-service-catalog-reference-architectures.s3.amazonaws.com/sagemaker/sc-portfolio-sagemaker.json)


### Install from your own S3 bucket  
1. clone this git repo:  
  ```git clone git@github.com:aws-samples/aws-service-catalog-reference-architectures.git```  
2. Copy everything in the repo to an S3 bucket:  
  ```cd aws-service-catalog-reference-architectures```  
  ```aws s3 cp . s3://[YOUR-BUCKET-NAME-HERE] --exclude "*" --include "*.json" --include "*.yml" --recursive```  
3. In the AWS [CloudFormation console](https://console.aws.amazon.com/cloudformation) choose "Create Stack" and supply the Portfolio S3 url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/sagemaker/sc-portfolio-sagemaker.json```  
5. Set the _LinkedRole1_ and _LinkedRole2_ parameters to any additional end user roles you may want to link to the Portfolio.
6. Set the _CreateEndUsers_ parameter to No if you have already run a Portfolio stack from this repo (ServiceCatalogEndusers already exists).
7. Change the _RepoRootURL_ parameter to your bucket's root url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/``` 


### Share an ML model with your organization
Often data scientists train an ML model which can be reused by other departments within the organization. Data scientists want to share these models for deployment with application teams and sagemaker_vend_endpoint.yml CloudFormation template allows you to do the same for real-time inference model deployment. The template accepts inference docker image path and model-artifact path, and creates an ML model. Then it creates an endpoint config and stands up an endpoint in a specific VPC.  

The IT administrator needs to do following steps to customize the template for a specific use-case:
1. Update <Docker Image path> on line 42 in sagemaker_vend_endpoint.yml with Docker registry path for the image that contains the inference code.
1. Update <Model Artifact S3:// path> on line 43 in sagemaker_vend_endpoint.yml with the S3 path where the model artifacts are stored.
1. Update the AllowedValues list for InstanceType parameter with appropriate values.
1. You can further specify template constraints for Subnet, security group, KMS key and the IAMExecution role to be associated with the ML model.
1. Once you have customized the template for a specific model, you can upload it to Amazon S3 and create a product and add it to appropriate portfolio that allows application teams/data scientists to consume the ml model.

Note: To use this template to share ml models across accounts, you  need to ensure that the artifact as well as the image are accessible in the destination account.