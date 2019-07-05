# Building an end-to-end IT lifecycle flow with AWS Service Catalog and ServiceNow

<img src="/labs/end-to-end-it-lifecycle-management/resources/sc-icon.png" width="400"><br/>
<img src="/labs/end-to-end-it-lifecycle-management/resources/snow-icon2.png" height="100">

In this workshop, cloud architects, Cloud Center of Excellence (CCOE) team members, and IT managers learn how to launch and operate governed cloud workloads on AWS by leveraging AWS management tools. They extend a sample catalog containing Amazon EC2 and enable catalog users to only manage the resources they create. They then perform the IT service management process integration using ServiceNow as an example solution.

This hands-on session requires you to **bring your own laptop and an AWS account with administrator access** to the workshop. 

Go through the sections below **in the order** provided to complete this lab.
## Steps

1. [Lab Overview](/labs/end-to-end-it-lifecycle-management/resources/LAB-OVERVIEW.md)

2. [Lab Setup](/labs/end-to-end-it-lifecycle-management/resources/LAB-SETUP.md)

3. **Lab Execution**
    1. [Deploy using AWS Service Catalog](/labs/end-to-end-it-lifecycle-management/resources/LAB-EXECUTION-1.md)
    2. [Integrate ServiceNow with AWS Service Catalog](/labs/end-to-end-it-lifecycle-management/resources/LAB-EXECUTION-2.md)
        1. [Configure your AWS accounts in ServiceNow](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-ACCOUNT-CONFIG.md) 
        2. [Provisioning AWS Services using ServiceNow](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-PROVISIONING.md)
        3. [Set up your AWS account to send notifications to ServiceNow](/labs/end-to-end-it-lifecycle-management/resources/README-AWS-NOTIFICATIONS-TO-SNOW.md)
        4. [Trigger incident creation in ServiceNow from AWS](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-INCIDENT-CREATION.md)
        5. [Remediate incident created in ServiceNow from AWS](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-INCIDENT-REMEDIATION.md)

## Clean Up

Congratulations! :tada: You have completed all the labs for building an end-to-end IT lifecycle flow with AWS Service Catalog and ServiceNow. 

**To make sure you are not charged for any unwanted services, you can clean up by deleting the stack created in the _Lab Setup_ stage and its resources.**

To delete the stack and its resources
1. From the AWS CloudFormation console in the region you used in the _Lab Setup_, select the stack that you created.
2. Click `Delete Stack`.
3. In the confirmation message that appears, click `Yes`, `Delete`.

At this stage, the status for your changes to `DELETE_IN_PROGRESS`. In the same way you monitored the
creation of the stack, you can monitor its deletion by using the `Events` tab. When AWS CloudFormation completes the deletion of the stack, it removes the stack from the list.

**If you need help cleaning up your AWS resources in this lab, reach out to your lab administrator.**

[(Back to top)](#building-an-end-to-end-IT-lifecycle-flow-with-AWS-Service-Catalog-and-ServiceNow)
## Contributing
Your contributions are always welcome! Please have a look at the [contribution guidelines](/labs/end-to-end-it-lifecycle-management/resources/CONTRIBUTING.md) first. :tada:

[(Back to top)](#building-an-end-to-end-IT-lifecycle-flow-with-AWS-Service-Catalog-and-ServiceNow)
## License
This sample code is made available under a modified MIT license. See the LICENSE file.

[(Back to top)](#building-an-end-to-end-IT-lifecycle-flow-with-AWS-Service-Catalog-and-ServiceNow)
