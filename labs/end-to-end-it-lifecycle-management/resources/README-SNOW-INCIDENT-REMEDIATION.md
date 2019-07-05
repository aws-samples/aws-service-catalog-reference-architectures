[⌂ Home](/labs/end-to-end-it-lifecycle-management/README.md)
<br />[< Back](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-INCIDENT-CREATION.md)

# Post Provisioned Operational Action Triggers Change Record in ServiceNow
In this section you will remediate the ServiceNow incident created in section d by updating the AWS Service Catalog provisioned product in ServiceNow’s My Assets (view of the CMDB) to the allowable web-server instance type. 

Update EC2 instance of size t2.medium to t2.micro from ServiceNow
1.	Go to the ServiceNow browser tab, on the top right of the screen, open the system administrator menu, and then Choose Impersonate User, choose SCEndUser01 as the impersonation.
2.	In the navigation panel on the left, search for My Assets, and choose My Assets (type My Assets in filter navigator search box) 
3.	Choose the Configuration Item (Product Name) that you requested in the previous task
![snow-remd-1](/labs/end-to-end-it-lifecycle-management/resources/snow-remd-1.png)

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
