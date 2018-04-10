# Service Catalog RDS Reference Architecture

This reference architecture demonstrates how an organization can leverage Serivce Catalog to provide Amazon Relation Database Service (RDS) databases testing and integration..  

## Getting Started

When implemented this reference architecture creates a Service Catalog Portfolio called "Service Catalog RDS Reference Architecture" with four associated products.  The Service Catalog Products reference RDS database cloudformation templates for PostgreSQL, MySQL, MariaDB, Microsoft SQL which can be lauched by end users through Service Catalog as either single instance databases or multi-availability zone databases.

### Single Instance Architecture

![sc-rds-ra-architecture-single-instance.png](sc-rds-ra-architecture-multi-az.png)


### Multi-Availability Zone Architecture

![sc-rds-ra-architecture-multi-az.png](sc-rds-ra-architecture-single-instance.png)

### Prerequisites

The following prerequisites are required:

1. Installation and configuration of the AWS Command Line Interface (CLI).  It is important to ensure that the AWS CLI configuration contains the correct target region as this region will be used to create the reference architecture components within Service Catalog.

    Instructions on installing and configurating the AWS Command Line Interface can be found on the AWS website at: https://aws.amazon.com/cli/

2. Access to a system with permission to execute a python script. The script utilizes modules for "boto3" and "random".

    Instructions on installing and configuring the boto3 python module can be found in the Boto 3 quickstart documentation at: http://boto3.readthedocs.io/en/latest/guide/quickstart.html

### Assumptions

* A Service Catalog has been enbaled in the target region.
* A Service Catalog Admin account has been created and assigned the "**AWSServiceCatalogAdminFullAccess**" IAM permission.
* A Service Catalog EndUser account has been created and assigned the "**AWSServiceCatalogEndUserFullAccess**" IAM permission.
* Testing of this reference architecture was conducted against Service Catalog VPC Reference Architecture which includes a VPC, 2 public Subnets, 2 private Subnets, IGW, Managed NAT GW, and an optional Linux bastion host. Additional information about the Service Catalog VPC Reference Architecture can be found here: https://s3.us-east-2.amazonaws.com/user_name-service-catalog-reference-architecture/vpc/README.md

### Installion Overview

1. Download the reference architecture zip file from S3 and expand its content into a folder.
2. Contents will include:
    * ./README.md (this file)
    * ./sc-rds-ra-setup.py (python script used during setup process)
    * ./sc-rds-postgresql-ra.yml (RDS PostgreSQL Cloudformation Template in YAML)
    * ./sc-rds-postgresql-ra.json (RDS PostgreSQL Cloudformation Template in JSON)
    * ./sc-rds-mysql-ra.yml (RDS MySQL Cloudformation Template in YAML)
    * ./sc-rds-mysql-ra.json (RDS MySQL Cloudformation Template in JSON)
    * ./sc-rds-mariadb-ra.yml (RDS MariaDB Cloudformation Template in YAML)
    * ./sc-rds-mariadb-ra.json (RDS MariaDB Cloudformation Template in JSON)
    * ./sc-rds-mssql-ra.yml (RDS Microsoft SQL Cloudformation Template in YAML)
    * ./sc-rds-mssql-ra.json (RDS Microsoft SQL Cloudformation Template in JSON)
    * ./sc-rds-ra-architecture-multi-az.png
    * ./sc-rds-ra-architecture-single-instance.png
3. Provide execute permissions to the python script.
4. Confirm AWS Region for deployment.
5. Execute the python setup script.

### Installation Step-By-Step

```text
### Download reference architecture
laptop:Downloads user_name$ mkdir ~/Downloads/sc-ra
laptop:Downloads user_name$ cd ~/Downloads/sc-ra
laptop:sc-ra user_name$ git clone https://github.com/aws-samples/aws-service-catalog-reference-architectures       

### Change to EC2 Reference Architecture directory
laptop:ec2 user_name$ cd rds     

### View Contents
laptop:rds user_name$ ls -l 
total 104
-rw-r--r--  1 user_name  staff    9285 Mar 13 10:38 README.md
-rw-r--r--  1 user_name  staff   11487 Mar 13 10:41 sc-rds-mariadb-ra.json
-rw-r--r--  1 user_name  staff    6558 Mar 12 10:48 sc-rds-mariadb-ra.yml
-rw-r--r--  1 user_name  staff   10681 Mar 13 10:42 sc-rds-mssql-ra.json
-rw-r--r--  1 user_name  staff    6236 Mar 12 10:48 sc-rds-mssql-ra.yml
-rw-r--r--  1 user_name  staff   11567 Mar 13 10:42 sc-rds-mysql-ra.json
-rw-r--r--  1 user_name  staff    6562 Mar 12 10:48 sc-rds-mysql-ra.yml
-rw-r--r--  1 user_name  staff   11804 Mar 13 10:42 sc-rds-postgresql-ra.json
-rw-r--r--  1 user_name  staff    6682 Mar 12 10:48 sc-rds-postgresql-ra.yml
-rw-r--r--  1 user_name  staff  148556 Mar 12 10:48 sc-rds-ra-architecture-multi-az.png
-rw-r--r--  1 user_name  staff  139535 Mar 12 10:48 sc-rds-ra-architecture-single-instance.png
-rwxr-xr-x  1 user_name  staff    7770 Mar 13 10:43 sc-rds-ra-setup.py

### Set execute permission on python setup script
laptop:rds user_name$ chmod +x sc-rds-ra-setup.py 

### Verify default AWS Region (this will be used for deployment)
laptop:rds user_name$ cat ~/.aws/config
[default]
region = us-east-2

### Execute the setup script 
laptop:rds user_name$ ./sc-rds-ra-setup.py 
STARTED -- Setup of Service Catalog RDS Reference Architecture.

PORTFOLIO CREATED: Service Catalog RDS Reference Architecture
--id=port-id
--arn=arn:aws:catalog:us-east-2:000000000000:portfolio/port-id

PRODUCT CREATED: Amazon RDS PostgreSQL Database
PRODUCT/PORTFOLIO ASSOCIATED: Amazon RDS PostgreSQL Database
--id=prod-id

PRODUCT CREATED: Amazon RDS MySQL Database
PRODUCT/PORTFOLIO ASSOCIATED: Amazon RDS MySQL Database
--id=prod-id

PRODUCT CREATED: Amazon RDS MariaDB Database
PRODUCT/PORTFOLIO ASSOCIATED: Amazon RDS MariaDB Database
--id=prod-id

PRODUCT CREATED: Amazon RDS Microsoft SQL Database
PRODUCT/PORTFOLIO ASSOCIATED: Amazon RDS Microsoft SQL Database
--id=prod-id

FINISHED -- Setup of Service Catalog RDS Reference Architecture.
```

### Service Catalog Portfolio Access

Once the setup script has completed there will be a new service catalog portfolio with four new products associated in the specified region.  Before these products can be launched access needs to be granted to the portfolio for the service catalog admin and end users.

1. Open the AWS Console in a browser window.
2. Select the Services dropdown from the upper left and navigate to the Service Catalog to open the Service Catalog management page.
3. Select the portfolio called "Service Catalog RDS Reference Architecture" to open the specific portfolio management page.
4. Expand the option for User, groups and roles and click "ADD USER, GROUP OR ROLE" which will open an access management page.  Select the specific users, groups and roles that you want to provide access to and click "ADD ACCESS".

### Service Catalog Product Launch

Once access has been provided to one or more end users the RDS reference architecture products can be lauched.  To lauch a RDS reference architecture product the user needs to log into Service Catalog, select the desired RDS Reference Architecture Product and click launch.  The launch process will ask the end user for various details about how the RDS product will be configured and where it will be deployed.  After the form fields are filled out and the product is launched Service Catalog will execute a cloudformation stack to build the product and provide the RDS database connection details back to the end user.

### Service Catalog RDS Reference Architecture Cleanup

To remove the RDS Reference Architecture from Service Catalog perform the following steps:

1. Terminate all Service Catalog RDS Reference Architecture provisioned products.
2. Remove all products from the portfolio.
3. Remove all constraints from the portfolio.**
3. Remove all access to users, groups and roles from the portfolio.
4. Remove all shares associated with the portfolio.**
4. Remove all tags from the portfolio.
5. Remove all tagOptions from the portfolio.**
5. Delete all products from Service Catalog.
5. Delete the porfolio from Service Catalog.

** These resources are not created as part of the setup process.

## Future Enhancements
* Add RDS Aurora
* Add RDS Oracle
* Add script to perform teardown
* Integrate products with CloudWatch
* Integrate products with AWS Instance Scheduler
* Integrate product launch into predefined baseline VPC

## Authors

* Israel Lawson - AWS Sr. Solutions Architect - Initial work

## License

* This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details

## Acknowledgments

The following AWS team members have provided guidance, code review and other assistance throughout the design of this reference architecture.

* David Aiken - AWS Solutions Architect Manager
* Mahdi - Service Calalog Business Development
* Phil Chen - AWS Sr. Solutions Architect
* Kanchan Waikar - AWS Solutions Architect
* Kenneth Walsh - AWS Solutions Architect

## Changelog

### 1.0
* Initial documentation created
* Added: README.md
* Added: sc-rds-ra.zip
* Added: sc-rds-mariadb-ra.yml   
* Added: sc-rds-mssql-ra.yml     
* Added: sc-rds-mysql-ra.yml     
* Added: sc-rds-postgresql-ra.yml
* Added: sc-rds-ra-architecture-multi-az.png  
* Added: sc-rds-ra-architecture-single-instance.png  
* Added: sc-rds-ra-setup.py

### 1.1
* Updated: README.md to use SC VPC Product instead of Quickstart VPC as reference
* Updated: sc-rds-ra-setup.py to use json template vs. yaml.
* Added: sc-rds-mariadb-ra.json   
* Added: sc-rds-mssql-ra.json     
* Added: sc-rds-mysql-ra.json     
* Added: sc-rds-postgresql-ra.json 
* Added: LICENSE
* Added: NOTICE
* Added: COPYING
