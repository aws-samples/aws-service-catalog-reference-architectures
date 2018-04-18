# Service Catalog EC2 Reference Architecture

This reference architecture demonstrates how an organization can leverage Serivce Catalog to provide Amazon Elastic Compute (EC2) instances and Simple Systems Manager (SSM) instance patching for testing and integration.

## Getting Started

When implemented this reference architecture creates a Service Catalog Portfolio called "Service Catalog EC2 Reference Architecture" with two associated products.  The Service Catalog Product references cloudformation templates for the Amazon EC2 Linux and Windows instances which can be lauched by end users through Service Catalog.  The Service Catalog EC2 product creates either an Aamzon Linux or Microsoft Windows EC2 instance in the VPC and Subnets selected by the end user.  A Amazon Simple Systems Manager patch baseline, maintenance window and task are created to allow for automated patching of the Aamzon Linux and Microsoft Windows operating systems.

### EC2 Architecture with Amazon Linux and Microsoft Windows instances

![sc-ec2-ra-architecture.png](sc-ec2-ra-architecture.png)

### For instructions on how to set up this Service catalog product and portfolio, see [How to set up Service Catalog Reference architecture products and portfolios section](https://github.com/aws-samples/aws-service-catalog-reference-architectures)

## License

* This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details

 
