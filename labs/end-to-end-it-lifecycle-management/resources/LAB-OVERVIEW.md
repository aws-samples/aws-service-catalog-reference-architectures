[< Back](/labs/end-to-end-it-lifecycle-management/README.md)
# Lab Overview
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

In this lab, you will learn the following things:<br />
_AWS Related_
1. Configure an approved catalog of IT services created and managed on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. 
2. The end user experience of provisioning and managing approved IT services using AWS Service Catalog.

_ServiceNow related_
1. Configure ServiceNow to connect with your AWS account and have access to your AWS Service Catalog portfolios and products
2. Configure ServiceNow to create security incidents based on SNS notifications from your AWS account 
2. Use ServiceNow to provision an Amazon EC2 instance through AWS Service Catalog in a standardized, and secure manner

### How does the architecture look?
![AWS-SC-SNOW-Architecture-Diagram](/labs/end-to-end-it-lifecycle-management/resources/architecture.png)


[Next: Lab Setup >>](/labs/end-to-end-it-lifecycle-management/resources/LAB-SETUP.md)
