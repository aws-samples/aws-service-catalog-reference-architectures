# AWS Service Catalog Glue Reference architecture

This reference architecture creates an AWS Service Catalog Portfolio called 
 "Service Catalog - AWS Glue Reference Architecture" with one associated product.
 The AWS Service Catalog Product references a cloudformation template for the
 a Glue Crawler which can be launched by end users through AWS Service Catalog.
 The AWS Service Catalog Glue product creates a crawler and a glue database. The crawler can be used to crawl S3 data source to populate the glue data catalog.

### Install  
Launch the Glue portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-Glue-Portfolio&templateURL=https://aws-service-catalog-reference-architectures.s3.amazonaws.com/glue/sc-portfolio-glue.json)



