# AWS Service Catalog Reference Blueprints

AWS Service Catalog allows you to centrally manage these commonly deployed IT services, and helps you achieve consistent governance 
and meet your compliance requirements, while enabling users to quickly deploy only the approved IT services they need. 
For more Information on AWS Service Catalog, see the 
[documentation](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).

Many organizations are looking for sample products that they can distribute to their IAM users for a specific use-case. 
The AWS Service Catalog Reference blueprints are sample products distributed via this GitHub repository that demonstrate
 specific use-cases around specific AWS Services. Note that these products have been tested in US-EAST-1 region.

To give you an example, the Amazon EC2 use case shows how an organization can leverage the AWS Service Catalog to provide
 Amazon Elastic Compute (EC2) instances and AWS Systems Manager (SSM)-based patching for testing and integration.
 The portfolio templates in each section will create a ServiceCatalog Portfolio with various products, a launch constraint and linked roles for execution.
 Currently GitHub repository contains the following reference blueprints:  
 1. [Virtual Private Cloud (VPC)](vpc)
 2. [Elastic Compute Cloud (EC2)](ec2)
 3. [Simple Storage Service (S3)](s3)
 4. [Relational Database Service (RDS)](rds)
 5. [Elastic MapReduce (EMR)](emr)

Note - Before you distribute the CloudFormation template to your organization, review the template and ensure that it is doing what you want it to do. Check IAM permissions, Deletion policies, update stack behavior, other aspects of the template, and ensure that they are as per your expectations and processes. These sample CloudFormation templates may need updates before you can use them in production.

### How to set up AWS Service Catalog Reference blueprint products and portfolios?
Each Blueprint comes with a detailed walkthrough guide that includes step-by-step instructions on how to set up the Service Catalog Blueprint. 

### Assumptions

* AWS Service Catalog has been set up in target AWS region.
* An AWS Service Catalog Admin IAM principal with "**AWSServiceCatalogAdminFullAccess**" managed policy associated has been created.
* An AWS Service Catalog End-user principal with "**AWSServiceCatalogEndUserFullAccess**" managed policy associated has been created.

### Installion - Overview  
To get started quickly you can click the "Launch Stack" button in each section.  Or, if you wish to modify files and execute from your own
S3 bucket then follow these instructions:  
1. clone this git repo:  
  ```git clone git@github.com:aws-samples/aws-service-catalog-reference-architectures.git```  
2. Copy everything in the repo to an S3 bucket:  
  ```cd aws-service-catalog-reference-architectures```  
  ```aws s3 cp . s3://[YOUR-BUCKET-NAME-HERE] --exclude ".git*" --recursive``` 
3. Contents will include directories for the following:
    * ./vpc 
    * ./ec2
    * ./s3
    * ./rds
    * ./emr
4. Navigate to the folder corresponding to the reference blueprint you wish to distribute via AWS Service Catalog
5. Review AWS Region you are currently in.
6. In the AWS [CloudFormation console](https://console.aws.amazon.com/cloudformation) choose "Create Stack" and supply the Portfolio's S3 url. 
For example the EC2 portfolio would be:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/ec2/sc-portfolio-ec2.json```  
7. If this is the first Portfolio you are creating then leave LaunchRoleName blank to allow CloudFormation to creat the launchconstraint role for you.
 If you have already run a portfolio template you should put the created launch constraint role name in the parameter field (default is SCEC2LaunchRole).
8. Set the "RepoRootURL" parameter to your bucket's root url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/```  
  
Once you create the stacks, an AWS Service Catalog portfolio containing reference blueprint product will be created. However, if you want to set up the portfolio manually, you can do so using AWS Service Catalog console.  

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
