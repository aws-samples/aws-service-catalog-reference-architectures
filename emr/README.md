# AWS Service Catalog EMR Reference blueprint

This reference architecture demonstrates how an organization can leverage AWS Serivce Catalog to provide Amazon Elastic MapReduce (EMR) clusters for testing and integration.

## Getting Started

When implemented this reference architecture creates an AWS Service Catalog Portfolio called "Service Catalog EMR Reference Architecture" with one associated product.  The AWS Service Catalog Product references a cloudformation template for the Amazon EMR cluster which can be lauched by end users through AWS Service Catalog.  The AWS Service Catalog EMR product creates an Aamzon Elastic MapReduce cluster in the VPC and Subnets selected by the end user.  A remote access security group is also created to allow for a bastion host to connect to the instances used by EMR via SSH.

[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-EMRPortfolio&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/emr/sc-portfolio-emr.json)

### Install from your own S3 bucket  
1. clone this git repo:  
  ```git clone git@github.com:aws-samples/aws-service-catalog-reference-architectures.git```  
1. Copy everything in the repo to an S3 bucket:  
  ```cd aws-service-catalog-reference-architectures```  
  ```aws s3 cp . s3://[YOUR-BUCKET-NAME-HERE] --exclude "*" --include "*.json" --include "*.yml" --recursive```  
2. In the AWS [CloudFormation console](https://console.aws.amazon.com/cloudformation) choose "Create Stack" and supply the Portfolio S3 url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/emr/sc-portfolio-emr.json```  
3. Set the _LinkedRole1_ parameter to your _SCProvisioningRole_ name.
4. Change the "RepoRootURL" parameter to your bucket's root url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/```


### Amazon Elastic MapReduce Cluster

![sc-emr-ra-architecture.png](sc-emr-ra-architecture.png)


### For detailed instructions on how to set up this AWS Service catalog product and portfolio, see [Walkthrough Guide](sc-emr-ra-walkthrough.pdf)


Note - Before you distribute this CloudFormation template, review the template and ensure that it is doing what you want it to do. Check IAM permissions, Deletion policies, and other aspects of the template to ensure that they are as per your expectations.


## License
This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details
Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

 
