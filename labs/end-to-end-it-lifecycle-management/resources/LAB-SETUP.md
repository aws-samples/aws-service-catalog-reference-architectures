[⌂ Home](/labs/end-to-end-it-lifecycle-management/README.md)
<br />[< Back](/labs/end-to-end-it-lifecycle-management/resources/LAB-OVERVIEW.md)

# 2. Lab Setup

### Infrastructure setup in your AWS account
You need an AWS account with Administrator access for successfully completing this lab.  If you do not have one, you can create an AWS account. For instructions on how to create an account, see following page- 
https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/
_(We will provide you AWS credits before you start at the day of this event for your AWS usage)_

You will need to setup your AWS account with the required infrastructure to run this lab. We have provided an AWS CloudFormation template to make this a one step process for you. Follow these steps to set up your AWS account for this lab:

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


### (SKIP FOR REINFORCE 2019) ServiceNow instance setup and configuration.
**Please skip this step if you are doing this as a part of AWS re:inforce 2019. We will provide you with a pre-configured ServiceNow instance for this event.** <br />
As a part of this lab, you will be connecting your `AWS account` with a `ServiceNow` instance. If you haven't been provided a `ServiceNow` instance, you can follow the [AWS Service Catalog-ServiceNow Connector Setup](README-PREREQ-SNOW.md) to set up a `ServiceNow` instance with the `AWS Service Catalog connector for ServiceNow` and a scoped app for setting up `SNS notifications`.

[Next: Lab Execution- AWS Related Activities >>](/labs/end-to-end-it-lifecycle-management/resources/LAB-EXECUTION-1.md)