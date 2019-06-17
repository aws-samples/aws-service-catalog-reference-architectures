[⌂ Home](/labs/end-to-end-it-lifecycle-management/README.md)
<br />[< Back](/labs/end-to-end-it-lifecycle-management/resources/LAB-SETUP.md)
# 3. Lab Execution
## Deploy using AWS Service Catalog
In this lab, you will go through the Service Catalog administrator and end-user experiences.
 <img src="/labs/end-to-end-it-lifecycle-management/resources/sc-icon.png" width="400"><br/>
We have set up pre-provisioned roles for you in the *Lab Setup* section. You will use these roles to perform tasks in the upcoming labs. The following roles have been created:
* User roles
    - `service_catalog_administrator`
    <br> This role has AWSServiceCatalogAdminFullAccess policy associated with it. You can use this user for configuring and managing your AWS Service Catalog.
    - `service_catalog_end_user`	
    <br> This role has AWSServiceCatalogEndUserFullAccess policy associated with it. You will use this user for launching products from available catalog.
### Task 1.1- Provisioning EC2 from the EC2 console 

1. Log in using the `Service Catalog end user` in your AWS account. To do this, use the link provided in the CloudFormation `Outputs` from the *Lab Setup* section for the key `SwitchRoleSCEndUser`.
2. We will now try to launch an EC2 instance from the [Amazon EC2 console](https://console.aws.amazon.com/ec2/v2/home).
3. Click on the `Launch Instance` button, and then click on `Select` for **any of the listed Amazon Machine Images (AMI)**.
4. Select the instance size of `t2.micro` and click `Review and Launch`.
5. On the `Review Instance Launch` page, click `Launch`.
6. For key pair, select `Proceed without a key pair` , and click `Launch Instances`.
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
    - Choose the menu for AWS Service Catalog on the left top corner, this will show you the left panel with options available for an administrator. 
    - Please see the sample screen below. Note: if you do not see a left panel as shown in the following screen, use chrome browser and reduce the resolution.
![sc-admin-view](/labs/end-to-end-it-lifecycle-management/resources/sc-admin-view.png)
5. Below the `Admin` section, click `Portfolios list`. The right panel will display all the portfolios available.
6. Click the `SNOW-SC Test Portfolio`. This will open the portfolio that was created for you.
![sc-portfolio-view](/labs/end-to-end-it-lifecycle-management/resources/sc-portfolio-view.png)
7. On the portfolio management screen of `SNOW-SC Test Portfolio`, notice that there is a product named `EC2 instance`. This was created for you during the _Lab Setup_ step. 
    - You may optionally click on the product to open it and subsequently on the version – V1.0 to see the CloudFormation template.
    - Whenever your end users request an EC2 instance using EC2 instance product, the AWS Service Catalog will run the CloudFormation template you configured and create a CloudFormation Stack.
8. On the portfolio management screen of `SNOW-SC Test Portfolio`, expand TagOptions. You will see that `cost-center=1001` tag-option has been associated with your portfolio. This means that any taggable product provisioned via users of this portfolio will have the `cost-center=1001` tag associated with it. You can click the `TagOption Library` option link to see your library of all tag-options configured across all portfolios.
9. On the portfolio management screen of `SNOW-SC Test Portfolio,` expand Constraints. 
    - Your end user - `service_catalog_end_user` does not have IAM permissions to create an EC2 instance as noted in _Task 1.1_. This user, however, has permissions to launch AWS Service Catalog products. 
    - When your end user launches an AWS Service Catalog product, a launch role with elevated permissions will be used by AWS Service Catalog to provision products. This is called a `Launch Constraint`.  
    - To enable your end user to launch approved instances, we have pre-configured a `Launch Constraint` that has permissions to create an EC2 instance with the product within the portfolio. 
    - Instead of having to provide direct EC2 IAM permissions to your end user, you are providing an elevated role that AWS Service Catalog will assume on behalf of the user for launching a preconfigured EC2 product. This will allow you to provide self-service to your end-users in a governed manner.

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
9. Click `NEXT`.
10. On the `TagOptions` page notice that cost-center has auto-populated. Click `NEXT`.
11. On the Notifications page, click `NEXT`.
12. On the Review page, review the configuration information, and click `LAUNCH`. This will create a CloudFormation stack. The initial status of the product is shown as `Under change`. Wait a minute, then refresh the screen till the status changes to `AVAILABLE`.
    -  This means you have successfully launched an EC2 instance from AWS Service Catalog. Optionally, you can review the EC2 instance you created. You have been given AmazonEC2ReadOnlyAccess so that you can view the EC2 Management Console.


[Next: Lab Execution- ServiceNow Related Activities >>](/labs/end-to-end-it-lifecycle-management/resources/LAB-EXECUTION-2.md)