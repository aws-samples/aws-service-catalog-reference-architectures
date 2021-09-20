# AWS Service Catalog RDS Reference architecture

This reference architecture creates an AWS Service Catalog Portfolio called
 "AWS Service Catalog RDS Reference Architecture" with four associated products.
 The AWS Service Catalog Products reference RDS database cloudformation templates for
 PostgreSQL, MySQL, MariaDB, Microsoft SQL which can be launched by end users through AWS
 Service Catalog as either single instance databases or multi-availability zone databases.

### Install  
Launch the RDS portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-RDSPortfolio&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/rds/sc-portfolio-rds.json)

  
### Single Instance Architecture  
![sc-rds-ra-architecture-multi-az.png](sc-rds-ra-architecture-single-instance.png)


### Multi-Availability Zone Architecture  
![sc-rds-ra-architecture-single-instance.png](sc-rds-ra-architecture-multi-az.png)

