# AWS Service Catalog EMR Reference blueprint

This reference architecture demonstrates how an organization can leverage AWS Serivce Catalog to provide Amazon Elastic MapReduce (EMR) clusters for testing and integration.

## Getting Started

When implemented this reference architecture creates an AWS Service Catalog Portfolio called "Service Catalog EMR Reference Architecture" with one associated product.  The AWS Service Catalog Product references a cloudformation template for the Amazon EMR cluster which can be lauched by end users through AWS Service Catalog.  The AWS Service Catalog EMR product creates an Aamzon Elastic MapReduce cluster in the VPC and Subnets selected by the end user.  A remote access security group is also created to allow for a bastion host to connect to the instances used by EMR via SSH.

### Amazon Elastic MapReduce Cluster

![sc-emr-ra-architecture.png](sc-emr-ra-architecture.png)


### For detailed instructions on how to set up this AWS Service catalog product and portfolio, see [Walkthrough Guide](sc-emr-ra-walkthrough.pdf)


Note - Before you distribute this CloudFormation template, review the template and ensure that it is doing what you want it to do. Check IAM permissions, Deletion policies, and other aspects of the template to ensure that they are as per your expectations.


## License

* This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details
Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

 
