[⌂ Home](/labs/end-to-end-it-lifecycle-management/README.md)
<br />[< Back](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-ACCOUNT-CONFIG.md)

# ServiceNow provisioning workflow
In this task, you will provision an AWS Service Catalog product for launching an EC2 instance from ServiceNow. 
You are now ready to order an EC2 instance from your ServiceNow service catalog.

## To validate the configuration of the Connector
1. Go to the ServiceNow browser tab, open the system administrator menu (Top right of the screen) and then Choose `Impersonate User`, choose `Abel Tuter` as the impersonation.
![snow-prov-1](/labs/end-to-end-it-lifecycle-management/resources/snow-prov-1.png)
2. Open Service Catalog under Self Service from the left navigation panel. This will display Service Catalog Home Screen. Choose AWS Service Catalog.
![snow-prov-2](/labs/end-to-end-it-lifecycle-management/resources/snow-prov-2.png)
3.	The user interface view displays the AWS Service Catalog category. 


## To order a product
1. Choose EC2 instance, then specify Product name as `My-Snow-EC2-Instance`.
![snow-prov-3](/labs/end-to-end-it-lifecycle-management/resources/snow-prov-3.png)

2. On the `Parameters` page, configure:
    - `KeyName`: Choose the key you created in task _Task 1.1_
    - `SubnetID`: **choose the value of 'PublicSubnetId' from the CloudFormation outputs noted in Lab Setup**
    - `InstanceType`: t2.medium
    - `Security Group`: **choose the value of 'SecurityGroup' from the CloudFormation outputs noted in Lab Setup**
    - `AMI`: **choose the value of 'AMI' from the CloudFormation outputs noted in Lab Setup**
6. Choose `Order Now` from Top Right of the screen. This will start the creation of an EC2 instance in your AWS account.
![snow-prov-4](/labs/end-to-end-it-lifecycle-management/resources/snow-prov-4.png)
7. Next, open `My Assets` from navigation panel in left.
8. Scroll down, and at the end of the page, under `My Asset Requests`, you can see the request number that you provisioned, under configuration item column.
![snow-prov-5](/labs/end-to-end-it-lifecycle-management/resources/snow-prov-5.png)
8. Click on `Provisioned Products` under the AWS Service Catalog navigation menu. Once product status becomes provisioned(you can refresh the screen in few seconds if you dont see this yet), you will see that `Request Termination` & `Request update` options have become available. This means that your EC2 instance has been launched.
![snow-prov-6](/labs/end-to-end-it-lifecycle-management/resources/snow-prov-6.png)

[Next: Set up AWS notifications to ServiceNow >>](/labs/end-to-end-it-lifecycle-management/resources/README-AWS-NOTIFICATIONS-TO-SNOW.md)