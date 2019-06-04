# Building an end-to-end IT lifecycle flow with AWS Service Catalog and ServiceNow

## **A. Lab Overview**

### What is AWS Service Catalog?
AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. AWS Service Catalog allows you to centrally manage commonly deployed IT services, and helps you achieve consistent governance and meet your compliance requirements, while enabling users to quickly deploy only the approved IT services they need.

**Service Catalog Concepts**
- A **product** is an IT service that you want to make available for deployment on AWS. You create a product by importing a CloudFormation template.
- A **provisioned product** is a CloudFormation stack. When an end user launches a product, the AWS Service Catalog provisions the product in form of a CloudFormation stack.
- A **portfolio** is a collection of products, together with the configuration information. You can use portfolios to manage the user access to specific products.
- **Constraints** control the way users can deploy a product.
    * _Launch Constraints_
    <br>With launchconstraints,you can specify a role that the AWS
    Service Catalog can assume to launch a product from the portfolio. This means that you don’t need to give permissions necessary to deploy the resource to your IAM user.
    * _Notification Constraints_ <br>A notification constraint specifies an Amazon SNS topic to receive notifications about stack events.
    * _Template Constraints_ <br>To limit the options that are available to end users when they launch a product, you apply template constraints.

### What are we doing in this lab?
This lab is designed to help you understand how AWS Service Catalog can help you meet your governance, security, and self-service objectives while running AWS workloads. Additionally, this lab will show you how AWS Service Catalog integrates with an asset management system like ServiceNow.

In this lab, you will learn the following things:
_AWS Related_
1. Configure an approved catalog of IT services created and managed on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. 
2. The end user experience of provisioning and managing approved IT services using AWS Service Catalog.

_ServiceNow related_
1. Configure ServiceNow to connect with your AWS account and have access to your AWS Service Catalog portfolios and products
2. Configure ServiceNow to create security incidents based on SNS notifications from your AWS account 
2. Use ServiceNow to provision an Amazon EC2 instance through AWS Service Catalog in a standardized, and secure manner

### How does the architecture look?
![AWS-SC-SNOW-Architecture-Diagram](/labs/end-to-end-it-lifecycle-management/resources/architecture.png)




## **B. Lab Setup**
### Infrastructure setup in your AWS account
You need an AWS account with Administrator access for successfully completing this lab.  If you do not have one, you can create an AWS account. For instructions on how to create an account, see following page- https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/ 
_(We will provide you AWS credits before you start at the day of this event for your AWS usage)_

You will need to setup your AWS account with the required infrastructure to run this lab. We have provided an AWS CloudFormation template to make this a one step process for you. Follow these steps to set up your AWS account for this lab:


>todo: Add Stack Template URL- upload lab.json to an S3 bucket  
1.	Login to your AWS account as an administrator and select one the following 4 regions from the top right corner on the AWS Management Console:
    - North Virginia (us-east-1)
    - Ireland (eu-west-1)
    - Singapore (ap-southeast-1)
    - Canada (ca-central-1)
<br />_Note - Ensure that you have AdministratorAccess policy attached with your login as you would be creating AWS resources including IAM roles and users._
2. Click on the `Launch Stack` button below to launch a Cloudformation template that will setup the required infrastructure in your AWS account.
<br />[![Launch Stack](/labs/end-to-end-it-lifecycle-management/resources/launch-stack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=SC-SNOW-&templateURL=https://marketplace-sa-resources.s3.amazonaws.com/lab.json)
3. On the `Create Stack` page, verify that you have selected one of the regions from _Step 1_ and Click `Next`.
6.	On the `Specify Details` page, enter `SC-SNOW-<your-name>` in the `Stack Name` text box, and then click `Next`. Do not change the parameter value for `PWD`. 
>todo- need to change the param name PWD or add explanation 
7.	On the `Options` page, click `Next`.
8.	On the `Review` page, select `"I acknowledge that AWS CloudFormation might create IAM resources with custom names."` checkbox and then click `Create`.
9.	Once status of the stack changes to `CREATE COMPLETE`, click on the stack and open the `Outputs` tab to see the output values.
10.	Copy the key and value column contents of the `Outputs` section and save it in a text file. You would be referring to these output values throughout the lab. Here are the keys that you will find in the output:
    ```
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
    ```
![Stack Complete](/labs/end-to-end-it-lifecycle-management/resources/stack-complete.png)


### ServiceNow instance setup and configuration.
**Please skip this step if you are doing this as a part of AWS re:inforce 2019. We will provide you with a pre-configured ServiceNow instance for this event.** <br />
As a part of this lab, you will be connecting your `AWS account` with a `ServiceNow` instance. If you haven't been provided a `ServiceNow` instance, you can follow the [AWS Service Catalog-ServiceNow Connector Setup](README-PREREQ-SNOW.md) to set up a `ServiceNow` instance with the `AWS Service Catalog connector for ServiceNow` and a scoped app for setting up `SNS notifications`.

>todo- lab folks will still need to configure SNOW with their AWS configuration



## **C. Lab Execution**
In this lab, we have set up pre-provisioned roles for you in the *Lab Setup* section. You will use these roles to perform tasks in the upcoming labs. The following roles have been created:
* User roles
    - ServiceCatalogAdministrator
    <br> This role has AWSServiceCatalogAdminFullAccess policy associated with it. You can use this user for configuring and managing your AWS Service Catalog.
    - ServiceCatalogEnduser
    <br> This role has AWSServiceCatalogEndUserFullAccess policy associated with it. You will use this user for launching products from available catalog.
### Task 1.1- Provisioning EC2 from the EC2 console 

1. Log in using the Service Catalog end user in your AWS account. To do this, use the link provided in the CloudFormation `Outputs` from the *Lab Setup* section for the key `SwitchRoleSCEndUser`.
2. From the AWS Management Console, click on `Services`, and select `EC2`
3. Click on the `Launch Instance` button, and then click on `Select` for any of the listed Amazon Machine Images (AMI).
4. Select the instance size of `t2.micro` and click `Review and Launch`.
5. On the `Review Instance Launch` page, click `Launch`.
6. Select an existing key pair, or create a new key pair for your instance, and click `Launch Instances`.
7. At this time, you will get the `Launch Failed` error. This is by design, and proves that your Service Catalog end user does not have the permissions to launch EC2 instances from the EC2 console.
![ec2-launch-fail](/labs/end-to-end-it-lifecycle-management/resources/ec2-fail.png)

In the next task, we will see how this user can launch an EC2 instance in a secure, and governed manner using AWS Service Catalog.

### Task 1.1- Provisioning EC2 from the EC2 console 




### Objective: Show the value prop of SNOW integration

1. Launch an EC2 instance from the ServiceNow dashboard 
2. Create an incident in ServiceNow if instance launched is t2.medium




***
Needs updates

## Clean Up
>todo

```sh
sample code
```

## Contributing
>todo

Your contributions are always welcome! Please have a look at the [contribution guidelines](CONTRIBUTING.md) first. :tada:

## License
This sample code is made available under a modified MIT license. See the LICENSE file.