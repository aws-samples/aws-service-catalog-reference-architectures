# AWS Service Catalog RDS Reference blueprint

This reference blueprint demonstrates how an organization can leverage Serivce Catalog to provide Amazon Relation Database Service (RDS) databases testing and integration..  

## Getting Started

When implemented this reference blueprint creates a AWS Service Catalog Portfolio called "AWS Service Catalog RDS Reference Architecture" with four associated products.  The AWS Service Catalog Products reference RDS database cloudformation templates for PostgreSQL, MySQL, MariaDB, Microsoft SQL which can be lauched by end users through AWS Service Catalog as either single instance databases or multi-availability zone databases.

### Single Instance Architecture  
![sc-rds-ra-architecture-multi-az.png](sc-rds-ra-architecture-single-instance.png)



### Multi-Availability Zone Architecture  
![sc-rds-ra-architecture-single-instance.png](sc-rds-ra-architecture-multi-az.png)

### For detailed instructions on how to set up this AWS Service catalog product and portfolio, see [Walkthrough Guide](sc-rds-ra-walkthrough.pdf)



Note - Before you distribute this CloudFormation template, review the template and ensure that it is doing what you want it to do. Check IAM permissions, Deletion policies, and other aspects of the template to ensure that they are as per your expectations.


## License

* This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details
Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
