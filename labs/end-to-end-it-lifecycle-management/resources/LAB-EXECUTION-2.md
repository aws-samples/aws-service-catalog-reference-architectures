[< Back](/labs/end-to-end-it-lifecycle-management/README.md)
# ServiceNow related activities
In this lab, you will go through the ServiceNow experience when integrated with AWS. 

 ![snow-icon](/labs/end-to-end-it-lifecycle-management/resources/snow-icon2.png)
### Task 2.1- Configure ServiceNow with access for your AWS account
In this task, you will add your AWS account specific information such as IAM user access keys, and secret access keys in ServiceNow. Please refer to the following page to go through these steps. 
[Configure your AWS accounts in ServiceNow](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-ACCOUNT-CONFIG.md) 

### Task 2.2- Provisioning an AWS Service Catalog for EC2 from ServiceNow
In this task, you will provision an AWS Service Catalog product for launching an EC2 instance from ServiceNow. 
Refer to the following page to go through these steps: 
[Provisioning AWS Services using ServiceNow](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-PROVISIONING.md)

### Task 2.3- Configure AWS to create incidents in ServiceNow
In this task, you will configure your AWS account to send an SNS notification to ServiceNow. 
We have preconfigured the AWS Config rule to evaluate if an EC2 instance other than size t2.micro is launc hed in your AWS account. You will enable this rule and set up an AWS CloudWatch events rule to trigger SNS notifications to ServiceNow from your account. 
Refer to the following page to go through the steps to enable notifications based on AWS Config: 
[Set up AWS notifications to ServiceNow](/labs/end-to-end-it-lifecycle-management/resources/README-AWS-NOTIFICATIONS-TO-SNOW.md)

### Task 2.4- Create an incident in ServiceNow by provisioning a disallowed EC2 instance size
In this task, you will use ServiceNow to launch an AWS Service Catalog product with an EC2 instance other than size t2.micro. This will trigger the AWS Config rule that we set up in the previous step, and generate a notification to create an incident in ServiceNow. Refer to the following page to go through the steps to trigger incident creation in ServiceNow: 
[Trigger incident creation in ServiceNow from AWS](README-SNOW-INCIDENT-CREATION.md)
