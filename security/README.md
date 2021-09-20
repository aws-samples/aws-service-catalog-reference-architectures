# AWS Service Catalog GuardDuty Reference architecture

This reference architecture creates an AWS Service Catalog Portfolio called 
 "Service Catalog - AWS GuardDuty Reference Architecture" with one associated product.
 The AWS Service Catalog Product references a cloudformation template for the
 a GuardDuty which can be launched by end users through AWS Service Catalog.
 The AWS Service Catalog GuardDuty product enables GuardDuty Delegated Aministrator account in all AWS Regions. GuardDuty findings across all regions are exported to aws-controltower-guardduty-[account id]-[region] bucket in the the Control Tower Log Archive account.

### Install  
Launch the GuardDuty portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-GuardDuty-Portfolio&templateURL=https://aws-service-catalog-reference-architectures.s3.amazonaws.com/security/sc-portfolio-gd.json)

