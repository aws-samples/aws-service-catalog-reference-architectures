## Use Service Catalog to deploy AWS Config Conformance Packs 

A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed as a single entity in an account and a Region or across an organization in AWS Organizations. Conformance packs are created by authoring a YAML template that contains the list of AWS Config managed or custom rules and remediation actions. The following templates are intended to be samples for using AWS Config rules and remediation actions within a conformance pack. They do not guarantee thorough compliance check as is. You need to modify the template by adding more AWS Config rules to meet your AWS Organizations requirements and ensuring thorough compliance of your AWS resources.

**Note** These conformance packs will be a part of the [Service Catalog Getting Started Library](https://console.aws.amazon.com/servicecatalog/home?#portfolios)

Conformance pack descriptions:

**sc_conformancepacks_prerequisites.yml**

  In order to utilize the Config Conformance Packs, step one is to execute this prerquisite template which will create an S3 bucket for all of the reporting associated to the conformance pack, as well as a service role that config conformance pack uses. Note- The Config Conformance Packs are intended to be samples for using AWS Config rules and remediation actions within a conformance pack. They do not guarantee thorough compliance check as is. You may need to modify the template by adding more AWS Config rules to meet your AWS Organizations requirements and ensuring thorough compliance of your AWS resources.


**sc_OperationalBestPracticesForAmazonDynamoDB.yaml**

This conformance pack assumes you have already installed the prerequisite template titled "AWS Config Conformance Packs- prerequisite". This template installs config rules to monitor for the best practices associated with DynamoDB environments. The following rules are included in the template - DynamoDbAutoscalingEnabled; DynamoDbTableEncryptionEnabled; and DynamoDbThroughputLimitCheck. Note- The Config Conformance Pack templates are intended to be samples for using AWS Config rules and remediation actions within a conformance pack. They do not guarantee thorough compliance check as is. You may need to modify the template by adding more AWS Config rules to meet your AWS Organizations requirements and ensuring thorough compliance of your AWS resources.

**sc_OperationalBestPracticesForPCI-DSS.yaml**

This conformance pack assumes you have already installed the prerequisite template titled "AWS Config Conformance Packs - prerequisite". This template installs the following 25 config rules to assist in monitoring compliance with PCI-DSS standards- DMSReplicationNotPublic; EBSSnapshotPublicRestorableCheck; EC2InstanceNoPublicIP; ElasticsearchInVPCOnly; IAMRootAccessKeyCheck; IAMUserMFAEnabled; IncomingSSHDisabled; InstancesInVPC; LambdaFunctionPublicAccessProhibited; LambdaInsideVPC; MFAEnabledForIAMConsoleAccess; RDSInstancePublicAccessCheck; RDSSnapshotsPublicProhibited; RedshiftClusterPublicAccessCheck; RestrictedIncomingTraffic; RootAccountHardwareMFAEnabled; RootAccountMFAEnabled; S3BucketBlacklistedActionsProhibited; S3BucketPolicyGranteeCheck; S3BucketPolicyNotMorePermissive; S3BucketPublicReadProhibited1; S3BucketPublicWriteProhibited; S3BucketVersioningEnabled; VPCDefaultSecurityGroupClosed; VPCSGOpenOnlyToAuthorizedPorts. Note-The Config Conformance Pack templates are intended to be samples for using AWS Config rules and remediation actions within a conformance pack. They do not guarantee thorough compliance check as is. You may need to modify the template by adding more AWS Config rules to meet your AWS Organizations requirements and ensuring thorough compliance of your AWS resources.

**sc_OperationalBestPracticesForAWSIdentityAndAccessManagement.yaml**

This conformance pack assumes you have already installed the prerequisite template titled "AWS Config Conformance Packs- prerequisite". This template installs config rules to monitor for the best practices associated with Identity and Access Management. The following Config rules are included with the template- IAMGroupHasUsersCheck; IAMPasswordPolicy; IAMPolicyBlacklistedCheck; IAMPolicyNoStatementsWithAdminAccess; IAMRoleManagedPolicyCheck; IAMRootAccessKeyCheck; IAMUserGroupMembershipCheck; IAMUserMFAEnabled; IAMUserNoPoliciesCheck; IAMUserUnusedCredentialsCheck; MFAEnabledForIAMConsoleAccess; RootAccountHardwareMFAEnabled; and, RootAccountMFAEnabled. Note-The Config Conformance Pack templates are intended to be samples for using AWS Config rules and remediation actions within a conformance pack. They do not guarantee thorough compliance check as is. You may need to modify the template by adding more AWS Config rules to meet your AWS Organizations requirements and ensuring thorough compliance of your AWS resources.
 
