[⌂ Home](/labs/end-to-end-it-lifecycle-management/README.md)
<br />[< Back](/labs/end-to-end-it-lifecycle-management/resources/LAB-EXECUTION-2.md)

# ServiceNow configuration with AWS accounts

In this workshop, for your convenience, the setup process has been simplified and some pre-configuration has been done for you. Also, following ServiceNow connection specific roles have been created for you:
- `SCEC2ConnectLaunchRole` - This role is an internal role created for your ServiceNow-Service Catalog
connector. This role is associated with EC2 product while setting up your SNOW-SC test portfolio.
- `SCWorkspacesConnectLaunchRole` - This role is an internal role created for your ServiceNow-Service Catalog connector. This role is associtaed with Workspaces product while setting up your SNOW-SC test portfolio.
- `SnowEndUser` - This role is mapped to the ServiceNow side role to which access to launch the products from a portfolio is given. This role has AWSServiceCatalogEndUserFullAccess managed policy associated with it and will have access to SNOW-SC test portfolio from your catalog.
- `SCSyncUser` - This user has ServiceCatalogAdminReadOnlyAccess policy associated it with. This user is used by Service catalog- Service now connector for synchronizing portfolios, products, etc.
- `SCEndUser` - Within ServiceNow, the SCEndUser is mapped to snow-stsuser-account. SCEndUser has access to assume SnowEndUser role.

In this task:
- You will configure the AWS Service Catalog Connector scoped application
- You will create two ServiceNow accounts, and map them to `SCEndUser` and `SCSyncUser` using their credentials.
- Next, you will run `Sync all accounts scheduled job` which will pull AWS Service Catalog resources into ServiceNow. 
- Next, you will associate SnowEndUser(fromAWS) with the snow-stsuser-account and order_aws_sc_products roles in ServiceNow.

## Configuring AWS Service Catalog Connector Scoped Application
>todo: Is this going to be preconfigured???

First, you must configure the AWS Service Catalog scoped application and applicable roles.
To configure the AWS Service Catalog scoped application and applicable roles
1.	Got to `User Administration` on the `ServiceNow`>`Roles`>`New`, create a role called `order_aws_sc_products`. This role is granted to any users with permission to order AWS Service Catalog products. For instructions, see Create a role. 
2.	Grant roles to the following users: 
    - `System Administrator (admin)`: For simplicity in this example, user admin is designated as the administrator of the AWS Service Catalog scoped application. Grant this user both of the administrative permissions from the adapter, `x_126749_aws_sc_portfolio_manager` and `x_126749_aws_sc_account_admin`. In a real scenario, these roles would likely be granted to two different users.
    - `Abel Tuter`: The user `abel.tuter` is chosen as an illustrative end user. Grant Abel the new role `order_aws_sc_products`. This allows him to order products from AWS.


## Configure accounts
In the AWS Service Catalog scoped app Accounts menu, you will create two accounts, one for sync and one for provisioning. 

The following table shows the correlations between AWS and ServiceNow identities:

| ServiceNow Account   | AWS User   |
|----------------------|------------|
| snow-sync-account    | SCSyncUser |
| snow-stsuser-account | SCEndUser  |

The `snow-stsuser-account` account will have no Regions configured. The `snow-sync-account` account has one region configured, matching the Region where the AWS Service Catalog is defined.

To configure `snow-sync-account`:
1. Log in to ServiceNow as the System Administrator using credentials provided to you (you will be given a link, and credentials for ServiceNow instance).
2. In the navigation panel on the left, choose `Accounts` (type `Accounts` in filter navigator search box) under AWS Service Catalog.
3. Choose `New` to create a new account.
![snow-acc-config-0](/labs/end-to-end-it-lifecycle-management/resources/snow-acc-config-0.png)
4. Specify `snow-sync-account` as the Name.
5. Under Access Key, specify the value of `SCSyncUserAccessKey` provided to you in the outputs section of Cloudformation.
6. Under Secret Access Key, specify the value of `SCSyncUserSAK` provided to you, in the outputs section of Cloudformation. Next, click on `Submit`, and open the `snow-sync-account`.
![snow-acc-config-1](/labs/end-to-end-it-lifecycle-management/resources/snow-acc-config-1.png)

7. Under Account Synchronizations, choose region specified in the output section by clicking the tick icon (you can double click on “insert a new row” in the Region column to see regions list) of Cloudformation and then click
on update.
8. Next, open the snow-sync-account entry. Choose Validate Regions, in a few seconds, it should show following message. 
![snow-acc-config-3](/labs/end-to-end-it-lifecycle-management/resources/snow-acc-config-3.png)
This means your ServiceNow is able to communicate with AWS.

To configure `snow-stsuser-account`:
1. Go back to Accounts screen, Choose New to create a new account.
2. Specify `snow-stsuser-account` as the Name.
3. Under Access Key, specify the value of `SCSyncUserAccessKey` provided to you in the outputs section of Cloudformation.
4. Under Secret Access Key, specify the value of `SCSyncUserSAK` provided to you, in the outputs section of Cloudformation. Next, click on `Submit`, and open the `snow-sync-account`.
![snow-acc-config-4](/labs/end-to-end-it-lifecycle-management/resources/snow-acc-config-4.png)

## Schedule Manual Sync
During the initial setup, manually execute the sync(synchronize) job instead of waiting for the Scheduled Jobs to occur. To synchronize the accounts manually, do the following:
1. As System Administrator, in ServiceNow console, find Scheduled Jobs under `System Definition` in the filter navigator panel on the left.
![snow-acc-config-5](/labs/end-to-end-it-lifecycle-management/resources/snow-acc-config-5.png)
2. Next, Search by name for job called `Sync all Accounts`, open it by clicking it, and then choose `Execute Now`.
![snow-acc-config-6](/labs/end-to-end-it-lifecycle-management/resources/snow-acc-config-6.png)

## Grant Access to Portfolios
Data will be visible in the AWS Service Catalog scoped app menus after the adapter’s scheduled synchronization job has run.
1. In ServiceNow, as an administrator user, in the navigation panel on the left, choose `Identities` under AWS Service Catalog.
2. Open the identity with `SnowEndUser` ARN. E.g. `arn:aws:iam::0123456789012:role/SnowEndUser`
3. Under Account, choose `snow-stsuser-account` (you can also find this by clicking on search/look-up button):, next, choose `Update` to update the record.
![snow-acc-config-7](/labs/end-to-end-it-lifecycle-management/resources/snow-acc-config-7.png)
4. Next, In ServiceNow, In the navigation panel on the left, choose `Role Grants` under AWS Service Catalog.
5. Choose `New `to create a new Role Grant. Under role, specify `order_aws_sc_products`.
6. Under `Identity`, specify SnowEndUser's ARN(you can also find this by clicking on search button) specified in the outputs section of Cloudformation, choose Submit.

### To test access to portfolios
1.	Choose the `Test Authorization` button shown in the AWS identity module.
2.	If the test is successful, the message `Successfully performed SearchProducts action as arn:aws:iam::AWS Account:role/SnowEndUser` is returned. 
![snow-acc-config-8](/labs/end-to-end-it-lifecycle-management/resources/snow-acc-config-8.png)
3.	An unsuccessful test returns the message `Error using account…`
4.	Given the preceding setup, `Abel Tuter` can now order products from AWS Service Catalog in ServiceNow.

[Next: Provisioning AWS Services using ServiceNow >>](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-PROVISIONING.md)