# AWS Service Catalog VPC Reference blueprint

This reference blueprint demonstrates how an organization can leverage AWS Service Catalog to provide Amazon Virtual Private Clouds (VPC) for testing and integration.  

## Getting Started

When implemented this reference blueprint creates an AWS Service Catalog Portfolio called "Service Catalog VPC Reference Architecture".  
The AWS Service Catalog Products reference cloudformation templates for the Amazon VPC which can be lauched by end users through 
AWS Service Catalog.  The product creates a VPC with two public and private subnets across two availability zones.  
The VPC includes an Internet Gateway and a managed NAT Gateway in each public subnet as well as VPC Route Tables and 
Network ACLs that allow for communication between the public and private subnets.  Optionally, an Amazon Linux bastion instance 
and a Security Group can be deployed into the public subnet to allow for remote connectivity to the bastion instance.

[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-VPCPortfolio&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/vpc/sc-portfolio-vpc.json)


### Multi-Availability Zone Architecture with Amazon Linux Bastion Instance

![sc-vpc-ra-architecture-multi-az.png](sc-vpc-ra-architecture-multi-az.png)


### For detailed instructions on how to set up this AWS Service catalog product and portfolio, see [Walkthrough Guide](sc-vpc-ra-walkthrough.pdf)

## License
Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
* This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details
