[⌂ Home](/labs/end-to-end-it-lifecycle-management/README.md)
<br />[< Back](/labs/end-to-end-it-lifecycle-management/resources/LAB-OVERVIEW.md)

# 2. Lab Setup

### Infrastructure setup in your AWS account
You need an AWS account with Administrator access for successfully completing this lab.  If you do not have one, you can create an AWS account. For instructions on how to create an account, see following page- 
https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/
_(We will provide you AWS credits before you start at the day of this event for your AWS usage)_

You will need to setup your AWS account with the required infrastructure to run this lab. We have provided an AWS CloudFormation template to make this a one step process for you. Follow these steps to set up your AWS account for this lab:

**Pre-requisites**:
- DO NOT use your ROOT user for this exercise.
- Create a user called *labadmin*, give it an an Administrator policy (optional if    you have a user with an admin policy)
- Login to your AWS Account using the *labadmin* user (or an admin user)



1.	Login to your AWS account as an administrator and select one the following 4 regions from the top right corner on the AWS Management Console:
    - North Virginia (us-east-1)
    - Ireland (eu-west-1)
    - Singapore (ap-southeast-1)
    - Canada (ca-central-1)
<br />_Note - Ensure that you have AdministratorAccess policy attached with your login as you would be creating AWS resources including IAM roles and users._
2. Click on the `Launch Stack` button below to launch a Cloudformation template that will setup the required infrastructure in your AWS account. (**CTRL + CLICK for opening this a new tab**)
<br />[![Launch Stack](/labs/end-to-end-it-lifecycle-management/resources/launch-stack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=SC-SNOW-&templateURL=https://reinforce-us-east-1.s3.amazonaws.com/lab_v2.json)
3. On the `Create Stack` page, verify that you have selected one of the regions from _Step 1_ and Click `Next`.
6.	On the `Specify Details` page, enter `SC-SNOW-<your-name>` in the `Stack Name` text box, and then click `Next`. 
7.	On the `Options` page, click `Next`.
8.	On the `Review` page, select `"I acknowledge that AWS CloudFormation might create IAM resources with custom names."` checkbox and then click `Create`.
9.	Once status of the stack changes to `CREATE COMPLETE`, click on the stack and open the `Outputs` tab to see the output values.
10.	Copy the key and value column contents of the `Outputs` section and save it in a text file. You would be referring to these output values throughout the lab. Here are the keys that you will find in the output:
    ```
    - ConfigBucket        
    - ConfigServiceRole
    - PublicSubnetId  
    - Region      
    - SCEC2ConnectLaunchRole       
    - ScheduledRule      
    - SecurityGroup   
    - SnowEndUser     
    - SwitchRoleAwsStudent
    - SwitchRoleSCAdmin   
    - SwitchRoleSCEndUser 
    - T2MicroConfigRuleTopic 
    ```
![Stack Complete](/labs/end-to-end-it-lifecycle-management/resources/stack-complete.png)

11. Now, you will go to AWS SSM parameter store, where we have **securely** stored the values of the IAM user access keys and secret access keys. Please copy these 4 values along with the values noted above, you will use them to set up your ServiceNow integration.
    1. Go to the `AWS Management Console`, and search for `Systems Manager`, and click on it. **Make sure you are in the same region from _Step 1_**.
    2. On the left navigation menu, click on `Parameter Store`.
    3. You will find the following four values stored in the parameter store:
        ```
        - SCEndUser-PublicAccessKey
        - SCEndUser-SecretAccessKey
        - SCSyncUser-PublicAccessKey
        - SCSyncUser-SecretAccessKey
        ```

![setup-ssm-1](/labs/end-to-end-it-lifecycle-management/resources/setup-ssm-1.png)

12. To access the value of these parameters, click on each of them, and check the `Value` field as shown below. For secret access keys, you will see the `Value` field masked since we have encrypted it for you. Just click on the `Show` button to display these keys. (Since you are logged in as the administrator, you can decrypt this value)
![setup-ssm-1.5](/labs/end-to-end-it-lifecycle-management/resources/setup-ssm-1.5.png)
![setup-ssm-2](/labs/end-to-end-it-lifecycle-management/resources/setup-ssm-2.png)

Please store all of the values in the previous step in a text file locally, since you will be needing them as we move through the labs.

### (SKIP FOR SUMMIT 2019) ServiceNow instance setup and configuration.
**Please skip this step if you are doing this as a part of an AWS Summit 2019. We will provide you with a pre-configured ServiceNow instance for this event.** <br />
As a part of this lab, you will be connecting your `AWS account` with a `ServiceNow` instance. If you haven't been provided a `ServiceNow` instance, you can follow the [AWS Service Catalog-ServiceNow Connector Setup](README-PREREQ-SNOW.md) to set up a `ServiceNow` instance with the `AWS Service Catalog connector for ServiceNow` and a scoped app for setting up `SNS notifications`.

[Next: Lab Execution- AWS Related Activities >>](/labs/end-to-end-it-lifecycle-management/resources/LAB-EXECUTION-1.md)
