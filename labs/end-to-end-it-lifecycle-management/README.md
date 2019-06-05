# Building an end-to-end IT lifecycle flow with AWS Service Catalog and ServiceNow

In this workshop, cloud architects, Cloud Center of Excellence (CCOE) team members, and IT managers learn how to launch and operate governed cloud workloads on AWS by leveraging AWS management tools. They extend a sample catalog containing Amazon EC2 and enable catalog users to only manage the resources they create. They then perform the IT service management process integration using ServiceNow as an example solution.

This hands-on session requires you to **bring your own laptop and an AWS account** to the workshop. 

## Table of Contents
[A. Lab Overview](#a.-lab-overview)
[B. Lab Setup](#b.-lab-setup)
[C. Lab Execution](#c.-lab-execution)
[Clean up](#clean-up)
[Contributing](#contributing)
[License](#license)
## **A. Lab Overview** 

### What is AWS Service Catalog?
AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. AWS Service Catalog allows you to centrally manage commonly deployed IT services, and helps you achieve consistent governance and meet your compliance requirements, while enabling users to quickly deploy only the approved IT services they need.

### What is ServiceNow?
ServiceNow is an enterprise service management platform that places a service oriented lens on the activities, tasks, and processes that make up day to day work life to enable a modern work environment. ServiceNow has a Service Catalog, which is a self-service application that end users can use to order IT services based on request fulfillment approvals and workflows.

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
    - `service_catalog_administrator`
    <br> This role has AWSServiceCatalogAdminFullAccess policy associated with it. You can use this user for configuring and managing your AWS Service Catalog.
    - `service_catalog_end_user`	
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

### Task 1.2- Admin experience of AWS Service Catalog
For your convenience, a sample catalog has been already set up for you. In this task, you will view the sample catalog and provision resources from the sample catalog.
1. Make sure that you are in the correct region by looking at value of Region from CloudFormation output you noted from the `Lab Setup` section. This is the region code that your lab has been set up for.
2. Switch your role to `service_catalog_administrator` by:
    - Copying the value of `SwitchRoleSCAdmin` from CloudFormation output you noted earlier
    - Pasting the value into the your browser tab
    - Clicking `Switch Role` button
3. Ensure you are in the same region as before in AWS Management Console.
4. On the Services menu, search and then choose `Service Catalog`.
    - The screen will be divided into two panels. Please see the sample screen below. Note: if you do not see a left panel as shown in the following screen, use chrome browser and reduce the resolution.
![sc-admin-view](/labs/end-to-end-it-lifecycle-management/resources/sc-admin-view.png)
5. Below the `Admin` section, click `Portfolios list`. The right panel will display all the portfolios available.
6. Click the `SNOW-SC Test Portfolio`. This will open the portfolio that was created for you.
![sc-portfolio-view](/labs/end-to-end-it-lifecycle-management/resources/sc-portfolio-view.png)
7. On the portfolio management screen of `SNOW-SC Test Portfolio`, notice that there is a product named `EC2 instance`. This was created for you during the _Lab Setup_ step. 
    - You may optionally click on the product to open it and subsequently on the version – V1.0 to see the CloudFormation template.
    - Whenever your end users request an EC2 instance using EC2 instance product, the AWS Service Catalog will run the CloudFormation template you configured and create a CloudFormation Stack.
8. On the portfolio management screen of `SNOW-SC Test Portfolio`, expand TagOptions. You will see that `cost-center=1001` tag-option has been associated with your portfolio. This means that any taggable product provisioned via users of this portfolio will have the `cost-center=1001` tag associated with it. You can click the `TagOption Library` option link to see your library of all tag-options configured across all portfolios.
9. On the portfolio management screen of `SNOW-SC Test Portfolio,` expand Constraints. Your end user - `service_catalog_end_user` does not have IAM permissions to create an EC2 instance as noted in _Task 1.1_. This is because you don’t want your end users to launch any EC2 instance. You only want them to launch EC2 instances that you have approved. 
    - To enable your end user to launch approved instances, we have pre-configured a role that has permissions to create an EC2 instance with the product(s) within the portfolio. 
    - Instead of having to give access to your end user, you can give an elevated role that AWS Service Catalog will assume on behalf of the user for that product. This will allow it to run the CloudFormation templates that you configured.

### Task 1.3- Provisioning EC2 from AWS Service Catalog
In this task, you will login as an end user and provision resources from the sample catalog we looked at in the previous step.
1. Make sure that you are in the correct region by looking at value of Region from CloudFormation output you noted from the `Lab Setup` section. This is the region code that your lab has been set up for.
2. Switch your role to `service_catalog_end_user` by:
    - Copying the value of `SwitchRoleSCEndUser` from CloudFormation output you noted earlier
    - Pasting the value into the your browser tab
    - Clicking `Switch Role` button
3. Ensure you are in the same region as before in AWS Management Console.
4. On the Services menu, search and then choose `Service Catalog`.
5. In the `Products list` page, click EC2 Instance, and then click `LAUNCH PRODUCT`.
6. On the `Product Version` page, configure:
    a. `Name`: My-EC2-instance
    b. Select `v1.0`
7. Click `NEXT`
8. On the `Parameters` page, configure:
    - `SubnetID`: **choose the value of 'PublicSubnetId' from the CloudFormation outputs noted in Lab Setup**
    - `InstanceType`: t2.micro
    - `Security Group`: **choose the value of 'SecurityGroup' from the CloudFormation outputs noted in Lab Setup**
    - `AMI`: **choose the value of 'AMI' from the CloudFormation outputs noted in Lab Setup**
9. Click `NEXT`.
10. On the `TagOptions` page notice that cost-center has auto-populated. Click `NEXT`.
11. On the Notifications page, click `NEXT`.
12. On the Review page, review the configuration information, and click `LAUNCH`. This will create a CloudFormation stack. The initial status of the product is shown as `Under change`. Wait a minute, then refresh the screen till the status changes to `AVAILABLE`.
    -  This means you have successfully launched an EC2 instance from AWS Service Catalog. Optionally, you can review the EC2 instance you created. You have been given AmazonEC2ReadOnlyAccess so that you can view the EC2 Management Console.


### Task 2.1- Configure ServiceNow with access for your AWS account
In this task, you will add your AWS account specific information such as IAM user access keys, and secret access keys in ServiceNow. Please refer to the following page to go through these steps. 
[Configure your AWS accounts in ServiceNow](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-ACCOUNT-CONFIG.md) 

### Task 2.2- Provisioning an AWS Service Catalog for EC2 from ServiceNow
In this task, you will provision an AWS Service Catalog product for launching an EC2 instance from ServiceNow. 
Refer to the following page to go through these steps: 
[Provisioning AWS Services using ServiceNow](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-PROVISIONING.md)

### Task 3.1- Configure AWS to create incidents in ServiceNow
In this task, you will configure your AWS account to send an SNS notification to ServiceNow. 
We have preconfigured the AWS Config rule to evaluate if an EC2 instance other than size t2.micro is launc hed in your AWS account. You will enable this rule and set up an AWS CloudWatch events rule to trigger SNS notifications to ServiceNow from your account. 
Refer to the following page to go through the steps to enable notifications based on AWS Config: 
[Set up AWS notifications to ServiceNow](/labs/end-to-end-it-lifecycle-management/resources/README-AWS-NOTIFICATIONS-TO-SNOW.md)

### Task 3.2- Create an incident in ServiceNow by provisioning a disallowed EC2 instance size
In this task, you will use ServiceNow to launch an AWS Service Catalog product with an EC2 instance other than size t2.micro. This will trigger the AWS Config rule that we set up in the previous step, and generate a notification to create an incident in ServiceNow. Refer to the following page to go through the steps to trigger incident creation in ServiceNow: 
[Trigger incident creation in ServiceNow from AWS](README-SNOW-INCIDENT-CREATION.md)


## Clean Up
>todo

```sh
add steps for clean up
```
[(Back to top)](#building-an-end-to-end-IT-lifecycle-flow-with-AWS-Service-Catalog-and-ServiceNow)
## Contributing
Your contributions are always welcome! Please have a look at the [contribution guidelines](/labs/end-to-end-it-lifecycle-management/resources/CONTRIBUTING.md) first. :tada:

[(Back to top)](#building-an-end-to-end-IT-lifecycle-flow-with-AWS-Service-Catalog-and-ServiceNow)
## License
This sample code is made available under a modified MIT license. See the LICENSE file.

[(Back to top)](#building-an-end-to-end-IT-lifecycle-flow-with-AWS-Service-Catalog-and-ServiceNow)