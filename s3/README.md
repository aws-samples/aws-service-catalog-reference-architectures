# Service Catalog EC2 Reference Architecture

This reference architecture demonstrates how an organization can leverage Serivce Catalog to provide Amazon Simple Storage Service (S3)) buckets with various configurations for testing and integration.

## Getting Started

When implemented this reference architecture creates a Service Catalog Portfolio called "Service Catalog S3 Reference Architecture" with five associated products.  The Service Catalog Product references cloudformation templates for the Amazon S3 buckets which can be lauched by end users through Service Catalog.  The Service Catalog S3 products create S3 buckets with varying configurations: 1) Read-Only bucket with access from anywhere, 2) Private bucket with access restricted to a source CIDR block, 3) Private bucket with access requiring multi-factor authentication, 4) Private bucket with contents encrypted with S3 server side encryption, and 5) Private bucket with a transition ruleset to migrate innactive objects to S3-IA and Glacier. 

### AWS S3 public Access read-only bucket

![sc-s3-public-ra-architecture.png](sc-s3-public-ra-architecture.png)

### AWS S3 private bucket with restricted access from source CIDR block

![sc-s3-cidr-ra-architecture.png](sc-s3-cidr-ra-architecture.png)

### AWS S3 Private SSE-S3 Encrypted Bucket

![sc-s3-encyprted-ra-architecture.png](sc-s3-encrypted-ra-architecture.png)

### AWS S3 Private MFA Restricted Access Bucket

![sc-s3-mfa-ra-architecture.png](sc-s3-mfa-ra-architecture.png)

### AWS S3 Private Bucket with transition policy for S3-IA and Glacier

![sc-s3-transition-ra-architecture.png](sc-s3-transition-ra-architecture.png)

### Prerequisites

The following prerequisites are required:

1. Installation and configuration of the AWS Command Line Interface (CLI).  It is important to ensure that the AWS CLI configuration contains the correct target region as this region will be used to create the reference architecture components within Service Catalog.

    Instructions on installing and configurating the AWS Command Line Interface can be found on the AWS website at: https://aws.amazon.com/cli/

2. Access to a system with permission to execute a python script. The script utilizes modules for "boto3" and "random".

    Instructions on installing and configuring the boto3 python module can be found in the Boto 3 quickstart documentation at: http://boto3.readthedocs.io/en/latest/guide/quickstart.html

3. Access to the ARN of the EndUser account used to access the Service Catalog as referenced in the assumptions seciton below.  The ARN will be used to assign access to the private access S3 buckets created with the Reference Architectures.

    Instructions on accessing the ARN for the Service Catalog EndUser via the CLI can be found here: https://docs.aws.amazon.com/cli/latest/reference/iam/get-user.html    

### Assumptions

* A Service Catalog has been enbaled in the target region.
* A Service Catalog Admin account has been created and assigned the "**AWSServiceCatalogAdminFullAccess**" IAM permission.
* A Service Catalog EndUser account has been created and assigned the "**AWSServiceCatalogEndUserFullAccess**" IAM permission.
* Access to the ARN of the EndUser account used to access the Service Catalog

### Installion Overview

1. Clone the reference architecture from Github and expand its content into a folder..
2. Contents will include:
    * ./README.md (this file)
    * ./COPYING
    * ./LICENSE
    * ./NOTICES
    * ./sc-s3-ra-setup.py (python script used during setup process)
    * ./sc-s3-public-ra.yml
    * ./sc-s3-encrypted-ra.yml
    * ./sc-s3-cidr-ra.yml
    * ./sc-s3-transition-ra.yml
    * ./sc-s3-mfa-ra.yml
    * ./sc-s3-public-ra.json
    * ./sc-s3-encrypted-ra.json
    * ./sc-s3-cidr-ra.json
    * ./sc-s3-transition-ra.json
    * ./sc-s3-mfa-ra.json
    * ./sc-s3-ra-architecture.png
3. Provide execute permissions to the python script.
4. Confirm AWS Region for deployment.
5. Execute the python setup script.

### Installation Step-By-Step

```text
### Download reference architecture
laptop:Downloads islawson$ mkdir ~/Downloads/sc-ra
laptop:Downloads islawson$ cd ~/Downloads/sc-ra
laptop:sc-ra islawson$ git clone https://github.com/aws-samples/aws-service-catalog-reference-architectures       

### Change to EC2 Reference Architecture directory
laptop:ec2 islawson$ cd s3        

### View Contents
laptop:s3 islawson$ ls -l
-rw-r--r--  1 islawson  staff  11357 Mar 22 16:20 COPYING
-rw-r--r--  1 islawson  staff  11357 Mar 22 16:20 LICENSE
-rw-r--r--  1 islawson  staff    121 Mar 22 16:20 NOTICES
-rw-r--r--  1 islawson  staff   8037 Mar 23 08:48 README.md
-rw-r--r--  1 islawson  staff   3259 Mar 23 15:42 sc-s3-cidr-ra.json
-rw-r--r--  1 islawson  staff   1440 Mar 23 13:28 sc-s3-cidr-ra.yml
-rw-r--r--  1 islawson  staff   3992 Mar 23 15:43 sc-s3-encrypted-ra.json
-rw-r--r--  1 islawson  staff   1738 Mar 23 12:49 sc-s3-encrypted-ra.yml
-rw-r--r--  1 islawson  staff   2851 Mar 23 15:42 sc-s3-mfa-ra.json
-rw-r--r--  1 islawson  staff   1280 Mar 23 13:24 sc-s3-mfa-ra.yml
-rw-r--r--  1 islawson  staff    939 Mar 23 15:43 sc-s3-public-ra.json
-rw-r--r--  1 islawson  staff    475 Mar 23 12:47 sc-s3-public-ra.yml
-rwxr-xr-x  1 islawson  staff   8752 Mar 22 17:16 sc-s3-ra-setup.py
-rw-r--r--  1 islawson  staff   3817 Mar 23 15:42 sc-s3-transition-ra.json
-rw-r--r--  1 islawson  staff   1952 Mar 23 12:47 sc-s3-transition-ra.yml

### Set execute permission on python setup script
laptop:s3 islawson$ chmod +x sc-ec2-ra-setup.py 

### Verify default AWS Region (this will be used for deployment)
laptop:s3 islawson$ cat ~/.aws/config
[default]
region = us-east-2

### Execute the setup script 
laptop:s3 islawson$ ./sc-ec2-ra-setup.py 

STARTED -- Setup of Service Catalog S3 Reference Architecture.

PORTFOLIO CREATED: Service Catalog S3 Reference Architecture
--id=port-lcxjv7k5d6bp2
--arn=arn:aws:catalog:us-east-1:384053732253:portfolio/port-lcxjv7k5d6bp2

PRODUCT CREATED: Amazon S3 Public Bucket with Read Only Access
PRODUCT/PORTFOLIO ASSOCIATED: Amazon S3 Public Access Read Only Bucket
--id=prod-6wmz3jiis63e4

PRODUCT CREATED: Amazon S3 Private Bucket with CIDR Restricted Access
PRODUCT/PORTFOLIO ASSOCIATED: Amazon S3 Private Bucket with CIDR Restricted Access
--id=prod-qagrnjswuadvg

PRODUCT CREATED: Amazon S3 Private Encrypted Bucket
PRODUCT/PORTFOLIO ASSOCIATED: Amazon S3 Encrypted Bucket
--id=prod-pxxplpa6qybao

PRODUCT CREATED: Amazon S3 Private Bucket with MFA Delete Restrictions
PRODUCT/PORTFOLIO ASSOCIATED: Amazon S3 Private Bucket with MFA Delete Restrictions
--id=prod-t34rnjg7bvfrk

PRODUCT CREATED: Amazon S3 Private Bucket with Transition Ruleset
PRODUCT/PORTFOLIO ASSOCIATED: Amazon S3 Private Bucket with Transition Ruleset
--id=prod-y4djwkxgf7dus

FINISHED -- Setup of Service Catalog S3 Reference Architecture.
```

### Service Catalog Portfolio Access

Once the setup script has completed there will be a new service catalog portfolio with a new S3 products associated in the specified region.  Before these products can be launched access needs to be granted to the portfolio for the service catalog admin and end users.

1. Open the AWS Console in a browser window.
2. Select the Services dropdown from the upper left and navigate to the Service Catalog to open the Service Catalog management page.
3. Select the portfolio called "Service Catalog S3 Reference Architecture" to open the specific portfolio management page.
4. Expand the option for User, groups and roles and click "ADD USER, GROUP OR ROLE" which will open an access management page.  Select the specific users, groups and roles that you want to provide access to and click "ADD ACCESS".

### Service Catalog Product Launch

Once access has been provided to one or more end users the S3 reference architecture product can be lauched.  To lauch a S3 reference architecture product the user needs to log into Service Catalog, select the S3 Reference Architecture Product and click launch.  The launch process will ask the end user for various details about how the S3 product will be configured.  After the form fields are filled out and the product is launched Service Catalog will execute a cloudformation stack to build the product and provide the S3 details back to the end user.

### Service Catalog S3 Reference Architecture Cleanup

To remove the S3 Reference Architecture from Service Catalog perform the following steps:

1. Terminate all Service Catalog S3 Reference Architecture provisioned products.
2. Remove all products from the portfolio.
3. Remove all constraints from the portfolio.**
3. Remove all access to users, groups and roles from the portfolio.
4. Remove all shares associated with the portfolio.**
4. Remove all tags from the portfolio.
5. Remove all tagOptions from the portfolio.**
5. Delete all products from Service Catalog.
5. Delete the porfolio from Service Catalog.

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
* Added ./README.md
* Added ./COPYING
* Added ./LICENSE
* Added ./NOTICES
* Added ./sc-s3-ra-setup.py
* Added ./sc-s3-public-ra.yml
* Added ./sc-s3-encrypted-ra.yml
* Added ./sc-s3-cidr-ra.yml
* Added ./sc-s3-transition-ra.yml
* Added ./sc-s3-mfa-ra.yml
* Added ./sc-s3-public-ra.json
* Added ./sc-s3-encrypted-ra.json
* Added ./sc-s3-cidr-ra.json
* Added ./sc-s3-transition-ra.json
* Added ./sc-s3-mfa-ra.json
* Added ./sc-s3-ra-architecture.png