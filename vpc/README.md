# AWS Service Catalog VPC Reference architecture

This reference architecture creates an AWS Service Catalog Portfolio called "Service Catalog VPC Reference Architecture". 
 The AWS Service Catalog Products reference cloudformation templates for the Amazon VPC which can be launched by end users through 
 AWS Service Catalog.  The product creates a VPC with two public and private subnets across two availability zones.  
 The VPC includes an Internet Gateway and a managed NAT Gateway in each public subnet as well as VPC Route Tables and 
 Network ACLs that allow for communication between the public and private subnets.  Optionally, an Amazon Linux bastion instance 
 and a Security Group can be deployed into the public subnet to allow for remote connectivity to the bastion instance.

 
### Install  
Launch the VPC portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-VPCPortfolio&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/vpc/sc-portfolio-vpc.json)
    * If you have already run the EC2 template, then you will put the _output.LaunchRoleName_ from the completed LaunchConstraintRole stack in the _LaunchRoleName_ field (default is SCEC2LaunchRole).  


### Multi-Availability Zone Architecture with Amazon Linux Bastion Instance

![sc-vpc-ra-architecture-multi-az.png](sc-vpc-ra-architecture-multi-az.png)
