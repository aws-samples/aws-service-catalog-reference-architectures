[⌂ Home](/labs/end-to-end-it-lifecycle-management/README.md)
<br />[< Back](/labs/end-to-end-it-lifecycle-management/resources/README-AWS-NOTIFICATIONS-TO-SNOW.md)

# Trigger incident creation in ServiceNow 
In this task, you will use ServiceNow to launch an AWS Service Catalog product with an EC2 instance other than size `t2.micro`. This will trigger the AWS Config rule that we set up in the previous step, and generate a notification to create an incident in ServiceNow. 
<br/>In the previous tasks, we set up an AWS Config Rule, AWS CloudWatch Event rule, and an AWS SNS notification to notify ServiceNow whenever an EC2 instance **OTHER** than `t2.micro` is launched. 
<br/>So, in this task, we will verify that an incident is created in ServiceNow by launching an EC2 instance of type `t2.medium`.

## Launch EC2 instance of size t2.medium from ServiceNow
1. Go to the ServiceNow browser tab, open the system administrator menu (Top right of the screen) and then Choose `Impersonate User`, choose `SCEndUser01` as the impersonation.
2. Go to the ServiceNow Service Catalog screen and choose AWS Service Catalog, choose EC2 instance, then specify Product name as `My-Snow-EC2-Instance-2`.
![snow-prov-3](/labs/end-to-end-it-lifecycle-management/resources/snow-prov-3.png)

3. On the `Parameters` page, configure:
    - `SubnetID`: **choose the value of 'PublicSubnetId' from the CloudFormation outputs noted in Lab Setup**
    - `InstanceType`: t2.medium
    - `Security Group`: **choose the value of 'SecurityGroup' from the CloudFormation outputs noted in Lab Setup**

4. Choose `Order Now` from Top Right of the screen. This will start the creation of an EC2 instance in your AWS account.
![snow-prov-4](/labs/end-to-end-it-lifecycle-management/resources/snow-prov-4.png)
5. Next, open `My Assets` from navigation panel in left.
6. Scroll down, and at the end of the page, under `My Asset Requests`, you can see the request number that you provisioned, under configuration item column.
![snow-prov-5](/labs/end-to-end-it-lifecycle-management/resources/snow-prov-5.png)
7. Click on `Provisioned Products` under the AWS Service Catalog navigation menu. Once product status becomes provisioned (you can refresh the screen in few seconds if you dont see this yet), you will see that `Request Termination` & `Request update` options have become available. This means that your EC2 instance has been launched.
![snow-prov-6](/labs/end-to-end-it-lifecycle-management/resources/snow-prov-6.png)

## Verify that an incident is created in the ServiceNow incidents screen
Now that you have launched an EC2 instance that makes Config rule non-compliant, you should be able to see an incident getting created in ServiceNow.
_Note_: 
- An AWS Config rule may take some time to run and report results. 
- If it is taking longer, open `AWS Config service` on the AWS screen, from the left panel, choose `rules`. Next, choose the `ConfigRuleForCheckIfInstanceIsNotOfTypeT2MicroVerification` rule to view the rule details. 
- Once you see evaluation details section populated with the newly non-compliant EC2 instance details, you are ready to check ServiceNow.

1. Go to the ServiceNow browser tab, open the system administrator menu (Top right of the screen) and then Choose `Impersonate User`, choose `System Administrator` as the impersonation.
2. In the left panel, type incidents and then choose `Incidents` available under `Service Desk` menu
![snow-incident-8](/labs/end-to-end-it-lifecycle-management/resources/snow-incident-8.png)
You will see an incident here, which means you have successfully integrated AWS SNS and ServiceNow.

[End- Go back home](/labs/end-to-end-it-lifecycle-management/README.md)
