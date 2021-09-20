# AWS Service Catalog EMR Reference architecture

This reference architecture creates an AWS Service Catalog Portfolio called 
 "Service Catalog EMR Reference Architecture" with one associated product.
 The AWS Service Catalog Product references a cloudformation template for the
 Amazon EMR cluster which can be launched by end users through AWS Service Catalog.
 The AWS Service Catalog EMR product creates an Amazon Elastic MapReduce cluster in the VPC and Subnets
 selected by the end user.  A remote access security group is also created to allow for a bastion host
 to connect to the instances used by EMR via SSH.

### Install  
Launch the EMR portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-EMRPortfolio&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/emr/sc-portfolio-emr.json)


### Amazon Elastic MapReduce Cluster

![sc-emr-ra-architecture.png](sc-emr-ra-architecture.png)

