# Service Catalog VPC Reference Architecture

This reference architecture demonstrates how an organization can leverage AWS Service Catalog to provide Amazon Virtual Private Clouds (VPC) for testing and integration.  

## Getting Started

When implemented this reference architecture creates an AWS Service Catalog Portfolio called "Service Catalog VPC Reference Architecture" containing product.  The Service Catalog Products reference cloudformation templates for the Amazon VPC which can be lauched by end users through Service Catalog.  The product creates a VPC with two public and private subnets across two availability zones.  The VPC includes an Internet Gateway and a managed NAT Gateway in each public subnet as well as VPC Route Tables and Network ACLs that allow for communication between the public and private subnets.  Optionally, an Amazon Linux bastion instance and a Security Group can be deployed into the public subnet to allow for remote connectivity to the bastion instance.

### Multi-Availability Zone Architecture with Amazon Linux Bastion Instance

![sc-vpc-ra-architecture-multi-az.png](sc-vpc-ra-architecture-multi-az.png)

### For instructions on how to set up this Service catalog product and portfolio, see [How to set up Service Catalog Reference architecture products and portfolios section](https://github.com/aws-samples/aws-service-catalog-reference-architectures)

## License

* This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details
