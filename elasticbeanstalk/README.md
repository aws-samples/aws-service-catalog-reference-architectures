# AWS Service Catalog Elastic Beanstalk Reference architecture

This reference architecture creates an AWS Service Catalog Portfolio called "Service Catalog Elastic Beanstalk Reference Architecture" with one associated product. The Service Catalog product references a CloudFormation template that deploys a web application bundle to a new Elastic Beanstalk environment.  To launch the environment, the user provides the web application name, the name of the S3 bucket where the web application is stored, and the name of the Elastic Beanstalk solution stack that the application will run on. A list of available Solution Stacks can be found here:
https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html

Get a list of Solution Stacks from the AWS CLI with this command:  
```aws elasticbeanstalk list-available-solution-stacks```


### Install  
Launch the Elastic Beanstalk portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-Beanstalk-Portfolio&templateURL=https://aws-service-catalog-reference-architectures.s3.amazonaws.com/elasticbeanstalk/sc-portfolio-elasticbeanstalk.json)


### Install from your own S3 bucket  
1. clone this git repo:  
  ```git clone git@github.com:aws-samples/aws-service-catalog-reference-architectures.git```  
2. Copy everything in the repo to an S3 bucket:  
  ```cd aws-service-catalog-reference-architectures```  
  ```aws s3 cp . s3://[YOUR-BUCKET-NAME-HERE] --exclude "*" --include "*.json" --include "*.yml" --recursive```  
3. In the AWS [CloudFormation console](https://console.aws.amazon.com/cloudformation) choose "Create Stack" and supply the Portfolio S3 url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/elasticbeanstalk/sc-portfolio-elasticbeanstalk.json```  
5. Set the _LinkedRole1_ and _LinkedRole2_ parameters to any additional end user roles you may want to link to the Portfolio.
6. Set the _CreateEndUsers_ parameter to No if you have already run a Portfolio stack from this repo (ServiceCatalogEndusers already exists).
7. Change the _RepoRootURL_ parameter to your bucket's root url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/``` 

