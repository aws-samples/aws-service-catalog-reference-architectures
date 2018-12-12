# AWS Service Catalog RDS Reference blueprint

This reference blueprint demonstrates how an organization can leverage Serivce Catalog to provide Amazon Relation Database Service (RDS) databases testing and integration..  

## Getting Started

When implemented this reference blueprint creates a AWS Service Catalog Portfolio called "AWS Service Catalog RDS Reference Architecture" with four associated products.  The AWS Service Catalog Products reference RDS database cloudformation templates for PostgreSQL, MySQL, MariaDB, Microsoft SQL which can be lauched by end users through AWS Service Catalog as either single instance databases or multi-availability zone databases.

[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-RDSPortfolio&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/rds/sc-portfolio-rds.json)

### Install from your own S3 bucket  
1. clone this git repo:  
  ```git clone git@github.com:aws-samples/aws-service-catalog-reference-architectures.git```  
1. Copy everything in the repo to an S3 bucket:  
  ```cd aws-service-catalog-reference-architectures```  
  ```aws s3 cp . s3://[YOUR-BUCKET-NAME-HERE] --exclude "*" --include "*.json" --include "*.yml" --recursive```  
2. In the AWS [CloudFormation console](https://console.aws.amazon.com/cloudformation) choose "Create Stack" and supply the Portfolio S3 url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/rds/sc-portfolio-rds.json```  
3. Set the "RepoRootURL" parameter to your bucket's root url:  
  ```https://s3.amazonaws.com/[YOUR-BUCKET-NAME-HERE]/```

### Single Instance Architecture  
![sc-rds-ra-architecture-multi-az.png](sc-rds-ra-architecture-single-instance.png)


### Multi-Availability Zone Architecture  
![sc-rds-ra-architecture-single-instance.png](sc-rds-ra-architecture-multi-az.png)

### For detailed instructions on how to set up this AWS Service catalog product and portfolio, see [Walkthrough Guide](sc-rds-ra-walkthrough.pdf)


Note - Before you distribute this CloudFormation template, review the template and ensure that it is doing what you want it to do. Check IAM permissions, Deletion policies, and other aspects of the template to ensure that they are as per your expectations.


## License
This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details
Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
