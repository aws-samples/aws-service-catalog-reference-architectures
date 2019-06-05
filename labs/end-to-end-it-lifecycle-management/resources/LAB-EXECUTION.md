# Lab Execution
In this lab, you will go through the Service Catalog administrator and end-user experiences in Section 1. In Section 2, you will go through the ServiceNow experience when integrated with AWS. 


## Section 1: AWS related activities
 ![sc-icon](/labs/end-to-end-it-lifecycle-management/resources/sc-icon.png)
We have set up pre-provisioned roles for you in the *Lab Setup* section. You will use these roles to perform tasks in the upcoming labs. The following roles have been created:
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

## Section 2- ServiceNow related activities
 ![snow-icon](/labs/end-to-end-it-lifecycle-management/resources/snow-icon.png)
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
