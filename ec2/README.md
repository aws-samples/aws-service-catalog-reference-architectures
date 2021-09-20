# AWS Service Catalog EC2 Reference architecture

This reference architecture creates an AWS Service Catalog Portfolio called "Service Catalog EC2 Reference Architecture" 
 with associated products. The AWS Service Catalog Product references cloudformation templates for the Amazon EC2 Linux and 
 Windows instances which can be launched by end users through AWS Service Catalog.  The AWS Service Catalog EC2 product creates 
 either an Amazon Linux or Microsoft Windows EC2 instance in the VPC and Subnets selected by the end user.
 A Amazon Simple Systems Manager patch baseline, maintenance window and task are created to allow for automated patching of the 
 Amazon Linux and Microsoft Windows operating systems. The Portfolio also includes a Linux webserver Product with either Apache or NGINX versions.

 
### Install  
Launch the EC2 portfolio stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-EC2DemoPortfolio&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/ec2/sc-portfolio-ec2demo.json)  
    * If you have already run the VPC template, then you will put the _output.LaunchRoleName_ from the completed LaunchConstraintRole stack in the _LaunchRoleName_ field (default is SCEC2LaunchRole).  

Be aware, running this service as demonstrated here is non-SSL http.  In production you must protect all web traffic with SSL.  
The example templates here cannot create and manage SSL for you, so it must be done as an additional task in your account.


### EC2 Architecture with Amazon Linux and Microsoft Windows instances

![sc-ec2-ra-architecture.png](sc-ec2-ra-architecture.png)


