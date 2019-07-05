[⌂ Home](/labs/end-to-end-it-lifecycle-management/README.md)
<br />[< Back](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-INCIDENT-CREATION.md)

## Post Provisioned Operational Action Triggers Change Record in ServiceNow
In this section you will remediate the ServiceNow incident created in section d by updating the AWS Service Catalog provisioned product in ServiceNow’s My Assets (view of the CMDB) to the allowable web-server instance type. 

# Update EC2 instance of size t2.medium to t2.micro from ServiceNow
1.	Go to the ServiceNow browser tab, on the top right of the screen, open the system administrator menu, and then Choose Impersonate User, choose SCEndUser01 as the impersonation.
2.	In the navigation panel on the left, search for My Assets, and choose My Assets (type My Assets in filter navigator search box) 
3.	Choose the Configuration Item (Product Name) that you requested in the previous task
![snow-remd-1](/labs/end-to-end-it-lifecycle-management/resources/snow-remd-1.png)
4.	Choose the Request Update for the product that you requested 
![snow-remd-2](/labs/end-to-end-it-lifecycle-management/resources/snow-remd-2.png)
5.	Choose the Request Update for the product that you requested.  Change the Instance Type from t2.medium to t2.micro
![snow-remd-3](/labs/end-to-end-it-lifecycle-management/resources/snow-remd-3.png)
6.	Choose the Update for the AWS Service Catalog product.  The product will go back to the My Asset view.  You will see a new Product Events entry with record type “Update_Provisioned_Product” 
![snow-remd-4](/labs/end-to-end-it-lifecycle-management/resources/snow-remd-4.png)
7.	Double-click on the change record.  Notice the post provisioned product update action resulted in a close change record in ServiceNow.  The product is now within the governed EC2 instance type.  
![snow-remd-5](/labs/end-to-end-it-lifecycle-management/resources/snow-remd-5.png)

[End- Go back home](/labs/end-to-end-it-lifecycle-management/README.md)
