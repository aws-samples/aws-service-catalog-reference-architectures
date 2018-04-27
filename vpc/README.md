Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
  
  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at
  
      http://www.apache.org/licenses/LICENSE-2.0
  
  or in the "license" file accompanying this file. This file is distributed 
  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
  express or implied. See the License for the specific language governing 
  permissions and limitations under the License.


# AWS Service Catalog VPC Reference blueprint

This reference blueprint demonstrates how an organization can leverage AWS Service Catalog to provide Amazon Virtual Private Clouds (VPC) for testing and integration.  

## Getting Started

When implemented this reference blueprint creates an AWS Service Catalog Portfolio called "Service Catalog VPC Reference Architecture".  The AWS Service Catalog Products reference cloudformation templates for the Amazon VPC which can be lauched by end users through AWS Service Catalog.  The product creates a VPC with two public and private subnets across two availability zones.  The VPC includes an Internet Gateway and a managed NAT Gateway in each public subnet as well as VPC Route Tables and Network ACLs that allow for communication between the public and private subnets.  Optionally, an Amazon Linux bastion instance and a Security Group can be deployed into the public subnet to allow for remote connectivity to the bastion instance.

### Multi-Availability Zone Architecture with Amazon Linux Bastion Instance

![sc-vpc-ra-architecture-multi-az.png](sc-vpc-ra-architecture-multi-az.png)

### For instructions on how to set up this AWS Service Catalog product and portfolio, see [How to set up AWS Service Catalog Reference blueprint products and portfolios section](https://github.com/aws-samples/aws-service-catalog-reference-architectures)

## License

* This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details
