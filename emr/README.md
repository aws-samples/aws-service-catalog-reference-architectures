Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
  
  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at
  
      http://www.apache.org/licenses/LICENSE-2.0
  
  or in the "license" file accompanying this file. This file is distributed 
  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
  express or implied. See the License for the specific language governing 
  permissions and limitations under the License.

# Service Catalog EMR Reference blueprint

This reference architecture demonstrates how an organization can leverage Serivce Catalog to provide Amazon Elastic MapReduce (EMR) clusters for testing and integration.

## Getting Started

When implemented this reference architecture creates a Service Catalog Portfolio called "Service Catalog EMR Reference Architecture" with one associated product.  The Service Catalog Product references a cloudformation template for the Amazon EMR cluster which can be lauched by end users through Service Catalog.  The Service Catalog EMR product creates an Aamzon Elastic MapReduce cluster in the VPC and Subnets selected by the end user.  A remote access security group is also created to allow for a bastion host to connect to the instances used by EMR via SSH.

### Amazon Elastic MapReduce Cluster

![sc-emr-ra-architecture.png](sc-emr-ra-architecture.png)

### For instructions on how to set up this Service catalog product and portfolio, see [How to set up Service Catalog Reference architecture products and portfolios section](https://github.com/aws-samples/aws-service-catalog-reference-architectures)


Note - Before you distribute this CloudFormation template, review the template and ensure that it is doing what you want it to do. Check IAM permissions, Deletion policies, and other aspects of the template to ensure that they are as per your expectations.


## License

* This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details

 
