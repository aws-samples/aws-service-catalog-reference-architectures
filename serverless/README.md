# AWS Service Catalog Serverless Reference architecture

This reference architecture creates a AWS Service Catalog Portfolio and sample product for creating AWS Lambda functions.  
End Users can create the Lambda function by supplying the S3 path to the code zip file and selecting basic settings for code runtime.


 
### Install  
Launch the Serverless portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-LambdaPortfolio&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/serverless/sc-portfolio-serverless.yml)
    

##Serverless Inc. Plugin 
this is a plugin for launching [serverless](https://www.serverless.com/) architecture from AWS Service Catalog.  
See the blog about the Serverless plugin for Service Catalog:
https://aws.amazon.com/blogs/apn/deploying-code-faster-with-serverless-framework-and-aws-service-catalog/

Plugin Repo: https://github.com/godaddy/serverless-aws-servicecatalog



