# Building an end-to-end IT lifecycle flow with AWS Service Catalog and ServiceNow
## **A. Lab Setup**
#### Infrastructure setup in your AWS account
You need an AWS account with Administrator access for successfully completing this lab.  If you do not have one, you can create an AWS account. For instructions on how to create an account, see following page- https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/ 
_(We will provide you AWS credits before you start at the day of this event for your AWS usage)_

You will need to setup your AWS account with the required infrastructure to run this lab. We have provided an AWS CloudFormation template to make this a one step process for you. Follow these steps to set up your AWS account for this lab:


>todo: Add Stack Template URL- upload lab.json to an S3 bucket  
1.	Login to your AWS account as an administrator and select one the following 4 regions from the top right corner on the AWS Management Console:
* North Virginia (us-east-1)
* Ireland (eu-west-1)
* Singapore (ap-southeast-1)
* Canada (ca-central-1)
_Note - Ensure that you have AdministratorAccess policy attached with your login as you would be creating AWS resources including IAM roles and users._
2. Click on the `Launch Stack` button below to launch a Cloudformation template that will setup the required infrastructure in your AWS account.
[![Launch Stack](/labs/end-to-end-it-lifecycle-management/resources/launch-stack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=SC-SNOW-&templateURL=https://github.com/aws-samples/aws-service-catalog-reference-architectures/blob/master/labs/end-to-end-it-lifecycle-management/cfn/lab.json)
3. On the `Create Stack` page, verify that you have selected one of the regions from _Step 1_ and Click `Next`.
6.	On the `Specify Details` page, enter `SC-SNOW-<your-name>` in the `Stack Name` text box, and then click `Next`. Do not change the parameter value for `PWD`. 
>todo- need to change the param name PWD or add explanation 
7.	On the `Options` page, click `Next`.
8.	On the `Review` page, select `"I acknowledge that AWS CloudFormation might create IAM resources with custom names."` checkbox and then click `Create`.
9.	Once status of the stack changes to `CREATE COMPLETE`, click on the stack and open the `Outputs` tab to see the output values.
10.	Copy the key and value column contents of the `Outputs` section and save it in a text file. You would be referring to these output values throughout the lab. Here are the keys that you will find in the output:
    - AMI         
    - ConfigBucket        
    - ConfigServiceRole
    - MySimpleAD
    - PublicSubnetId  
    - Region      
    - SCEC2ConnectLaunchRole  
    - SCEndUserAccessKey
    - SCEndUserSAK        
    - ScheduledRule   
    - SCSyncUserAccessKey         
    - SCSyncUserSAK       
    - SecurityGroup   
    - SnowEndUser     
    - SwitchRoleAwsStudent
    - SwitchRoleSCAdmin   
    - SwitchRoleSCEndUser 
    - T2MicroConfigRuleTopic    
    - T2MicroConfigRuleTopic       

![Stack Complete](/labs/end-to-end-it-lifecycle-management/resources/stack-complete.png)




#### ServiceNow instance setup and configuration.
**Please skip this step if you are doing this as a part of AWS re:inforce 2019. We will provide you with a pre-configured ServiceNow instance for this event.**
As a part of this lab, you will be connecting your `AWS account` with a `ServiceNow` instance. If you haven't been provided a `ServiceNow` instance, you can follow the [AWS Service Catalog-ServiceNow Connector Setup](README-PREREQ-SNOW.md) to set up a `ServiceNow` instance with the `AWS Service Catalog connector for ServiceNow` and a scoped app for setting up `SNS notifications`.

>todo- lab folks will still need to configure SNOW with their AWS configuration

## **B. Lab Overview**
#### What are we doing in this lab?
AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. AWS Service Catalog allows you to centrally manage commonly deployed IT services in AWS, and helps you achieve consistent governance and meet your compliance requirements while enabling users to quickly deploy only the approved IT services they need.
In this lab, you will learn the following things:

_AWS Related_
1. Configure an approved catalog of IT services created and managed on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. 
2. The end user experience of provisioning and managing approved IT services using AWS Service Catalog.

_ServiceNow related_
1. Configure ServiceNow to connect with your AWS account and have access to your AWS Service Catalog portfolios and products
2. Configure ServiceNow to create security incidents based on SNS notifications from your AWS account 
2. Use ServiceNow to provision an Amazon EC2 instance through AWS Service Catalog in a standardized, and secure manner

#### How does the architecture look?
![AWS-SC-SNOW-Architecture-Diagram](/labs/end-to-end-it-lifecycle-management/resources/architecture.png)



## **C. Lab Execution**

#### Objective: Show the value prop of AWS SC

1. Try to launch an EC2 instance from the console--get error
2. Launch through Service Catalog in a controlled fashion--shows value prop of AWS SC

#### Objective: Show the value prop of SNOW integration

1. Launch an EC2 instance from the ServiceNow dashboard 
2. Create an incident in ServiceNow if instance launched is t2.medium




***
Needs updates

## Clean Up

[(Back to top)](#table-of-contents)

>todo

```sh
sample code
```

## Contributing
[(Back to top)](#table-of-contents)
>todo

Your contributions are always welcome! Please have a look at the [contribution guidelines](CONTRIBUTING.md) first. :tada:

## License

[(Back to top)](#table-of-contents)

>todo