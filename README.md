# AWS Service Catalog Reference Architectures

These reference architectures demonstarte how an organization can leverage AWS Service Catalog to create and manage catalogs of IT services that are approved for use on AWS. These reference architectures include Virtual Private Cloud (VPC), Elastic Compute Cloud (EC2), Simple Storage Service (S3), Relational Database Service (RDS), and Elastic MapReduce (EMR).  AWS Service Catalog allows you to centrally manage these commonly deployed IT services, and helps you achieve consistent governance and meet your compliance requirements, while enabling users to quickly deploy only the approved IT services they need.

## Getting Started

When implemented this reference architecture creates a Service Catalog Portfolio called "Service Catalog VPC Reference Architecture" with one associated product.  The Service Catalog Products reference cloudformation templates for the Amazon VPC which can be lauched by end users through Service Catalog.  The Service Catalog VPC product creates a VPC with two public and private subnets across two availability zones.  The VPC includes an Internet Gateway and a managed NAT Gateway in each public subnet as well as VPC Route Tables and Network ACLs that allow for communication between the public and private subnets.  Optionally, an Amazon Linux bastion instance and a Security Group can be deployed into the public subnet to allow for remote connectivity to the bastion instance.

### Installion Overview

1. Clone the reference architecture from Github into a folder.
2. Contents will include directories for the following:
    * ./vpc 
    * ./ec2
    * ./s3
    * ./rds
    * ./emr
3. Navigate to the service you are interested in deploying
4. Confirm AWS Region for deployment.
5. Execute the python setup script.

### Service Catalog Portfolios

AWS Service Catalog portfolios will be created for each of the reference architectues.  These portfolios contain the Service Catalog products created from the cloudformation templates provided for each service.  Portfolios can be administered to include the management of users, application of constraints, tagging of portfolios and products, and the sharing of porfolios and products with other accounts.

![sc-ra-portfolios.png](sc-ra-portfolios.png)

### Service Catalog Product Launch

AWS Service Catalog products will be created within each reference architecture portfolio.  These products are available for Service Catalog EndUsers to launch.  The launch process will ask the end user for various details about how the product will be configured.  After the form fields are filled out and the product is launched Service Catalog will execute a cloudformation stack to build the product and provide the outputs related to the product back to the end user.  These outputs are used to access the resources created during the launch of the product.

![sc-ra-products.png](sc-ra-products.png)

## License

* This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details

## Authors

* Israel Lawson - AWS Sr. Solutions Architect - Initial work

## Acknowledgments

The following AWS team members have provided guidance, code review and other assistance throughout the design of this reference architecture.

* David Aiken - AWS Solutions Architect Manager
* Mahdi - Service Calalog Business Development
* Phil Chen - AWS Sr. Solutions Architect
* Kanchan Waikar - AWS Solutions Architect
* Kenneth Walsh - AWS Solutions Architect