# AWS Service Catalog EC2 Reference blueprint

This reference blueprint demonstrates how an organization can leverage Serivce Catalog to provide Amazon Elastic Compute (EC2) instances and Simple Systems Manager (SSM) instance patching for testing and integration.

## Getting Started

When implemented this reference blueprint creates an AWS Service Catalog Portfolio called "Service Catalog EC2 Reference Architecture" with two associated products.  The AWS Service Catalog Product references cloudformation templates for the Amazon EC2 Linux and Windows instances which can be lauched by end users through AWS Service Catalog.  The AWS Service Catalog EC2 product creates either an Aamzon Linux or Microsoft Windows EC2 instance in the VPC and Subnets selected by the end user.  A Amazon Simple Systems Manager patch baseline, maintenance window and task are created to allow for automated patching of the Aamzon Linux and Microsoft Windows operating systems.

### Try it yourself

1. clone this git repo:  
  ```git clone git@github.com:aws-samples/aws-service-catalog-reference-architectures.git```  
1. Copy everything in the repo to an S3 bucket:  
  ```cd aws-service-catalog-reference-architectures```  
  ```aws s3 cp . s3://[YOUR-BUCKET-NAME-HERE] --exclude ".git*" --recursive```  
2. In the AWS [CloudFormation console](https://console.aws.amazon.com/cloudformation) choose "Create Stack" and supply the Portfolio S3 url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/ec2/sc-portfolio-ec2.json```  
3. Set the "RepoRootURL" parameter to your bucket's root url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/```  
  
Or, just click this button:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-EC2Portfolio&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/ec2/sc-portfolio-ec2.json)

You can see the programatic way to create portfolios and products using python in [sc-ec2-ra-setup.py](sc-ec2-ra-setup.py)


### EC2 Architecture with Amazon Linux and Microsoft Windows instances

![sc-ec2-ra-architecture.png](sc-ec2-ra-architecture.png)

### For instructions detailed instructions on how to set up this AWS Service catalog product and portfolio, see [Walkthrough Guide](sc-ec2-ra-walktrough.pdf)

Note - Before you distribute this CloudFormation template, review the template and ensure that it is doing what you want it to do. Check IAM permissions, Deletion policies, and other aspects of the template to ensure that they are as per your expectations.


## License

Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.  
This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details  

 
