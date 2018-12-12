# AWS Service Catalog Reference Blueprints

AWS Service Catalog allows you to centrally manage these commonly deployed IT services, and helps you achieve consistent governance and meet your compliance requirements, while enabling users to quickly deploy only the approved IT services they need. For more Information on AWS Service Catalog, see [documentation](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html)

Many organizations are looking for sample products that they can distribute to their IAM users for a specific use-case. The AWS Service Catalog Reference blueprints are sample products distributed via this GitHub repository that demonstrate specific use-cases around specific AWS Services. Note that these products have been tested in US-EAST-1 region.

To give you an example, the Amazon EC2 use case shows how an organization can leverage the AWS Service Catalog to provide Amazon Elastic Compute (EC2) instances and AWS Systems Manager (SSM)-based patching for testing and integration. Currently GitHub repository contains following reference blueprints: 
 1. [Virtual Private Cloud (VPC)](vpc)
 2. Elastic Compute Cloud (EC2)
 3. Simple Storage Service (S3)
 4. Relational Database Service (RDS)
 5. Elastic MapReduce (EMR).  

Note - Before you distribute the CloudFormation template to your organization, review the template and ensure that it is doing what you want it to do. Check IAM permissions, Deletion policies, update stack behavior, other aspects of the template, and ensure that they are as per your expectations and processes. These sample CloudFormation templates may need updates before you can use them in production.


### How to set up AWS Service Catalog Reference blueprint products and portfolios?
Each Blueprint comes with a detailed walkthrough guide that includes step-by-step instructions on how to set up the Service Catalog Blueprint. 

### Pre-requisites

1. AWS CLI configured to point to the region in which you want to create the reference blueprint components within AWS Service Catalog.  
2. Access to a system with permissions to execute a python script. The script utilizes "boto3" and "random" modules.  

### Assumptions

* AWS Service Catalog has been set up in target AWS region.
* An AWS Service Catalog Admin IAM principal with "**AWSServiceCatalogAdminFullAccess**" managed policy associated has been created.
* An AWS Service Catalog End-user principal with "**AWSServiceCatalogEndUserFullAccess**" managed policy associated has been created.

### Installion - Overview

1. Using your terminal, clone the reference blueprint from Github into a folder.
2. Contents will include directories for the following:
    * ./vpc 
    * ./ec2
    * ./s3
    * ./rds
    * ./emr
3. Navigate to the folder corresponding to the reference blueprint you wish to distribute via AWS Service Catalog
4. Review AWS Region you are currently in.
5. Review the python script, modify necessary parameters, and finally execute the python setup script.

### Installation -  Step-By-Step instructions
Here is the list of commands to be executed from terminal - 
```text
### Download reference blueprint
mkdir ~/Downloads/sc-ra
cd ~/Downloads/sc-ra
git clone https://github.com/aws-samples/aws-service-catalog-reference-architectures       

### Change to appropriate Reference blueprint directory, these instructions show how to create VPC Service Catalog product. However instructions remain identical for all reference blueprint modules.
cd vpc      

### You can execute ls -l if you are using linux terminal to see files available.
ls -l
-rw-r--r--  1 username  staff   #### Mar 12 16:07 README.md
-rwxr-xr-x  1 username  staff   #### Mar 12 15:19 sc-vpc-ra-setup.py
-rw-r--r--  1 username  staff  ##### Mar 12 16:10 sc-vpc-ra.json
-rw-r--r--  1 username  staff  ##### Mar 12 16:00 sc-vpc-ra.yml
-rw-r--r--  1 username  staff ###### Mar 12 17:53 sc-vpc-ra-architecture-multi-az.png

### Set execute permissions on an appropriate python setup script
chmod +x sc-vpc-ra-setup.py 

### Verify whether your CLI is configured for appropriate region. Note that the script will create an AWS Service Catalog product along with corresponding portfolio. 
cat ~/.aws/config
[default]
region = us-east-2

### Execute the setup script 
Before you execute the script, review and revisit the parameters defined in the python script.
./sc-vpc-ra-setup.py 
```

Once you execute python script, an AWS Service Catalog portfolio containing reference blueprint product will be created. However, if you want to set up the portfolio manually, you can do so using AWS Service Catalog console.

![sc-ra-portfolios.png](sc-ra-portfolios.png)

Once you have set up the portfolio, you would need to grant end-users access. To know more about how to grant access, see [documentation](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-iamenduser.html)
### AWS Service Catalog Product Launch

Once access has been provided to one or more end users, the reference blueprint product can be lauched.  To know more about how to launch AWS Service Catalog product, see 
[documentation](https://docs.aws.amazon.com/servicecatalog/latest/userguide/enduser-launch.html)

![sc-ra-products.png](sc-ra-products.png)

## License

Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
* This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details

## Authors

* Israel Lawson - AWS Sr. Solutions Architect - Initial work

## Acknowledgments

The following AWS team members have provided guidance, code review and other assistance throughout the design of this reference blueprint.

* David Aiken - AWS Solutions Architect Manager
* Mahdi Sajjadpour - AWS Service Catalog Business Development
* Phil Chen - AWS Sr. Solutions Architect
* Kanchan Waikar - AWS Solutions Architect
* Kenneth Walsh - AWS Solutions Architect
