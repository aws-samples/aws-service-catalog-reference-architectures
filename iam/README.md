# AWS Service Catalog IAM Roles and Groups

The roles in this section support the launching of ServiceCatalog Products as launch constraints.
You can create them all at once or individually depending on the portfolio you are deploying.
The EndUser Policy and group is used by all portfolios and should be created before any Portfolios.

See the
 [ServiceCatalog IAM Guide](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-iamenduser.html) for more details.
 Users, groups, and roles which will be provisioning Service Catalog products must have the
 **AWSServiceCatalogEndUserFullAccess** managed policy attached. If you have other roles which you want to give access to a
 portfolio, then use _LinkedRole1_ and _LinkedRole2_. If you wish to add other users or groups directly, then modify the portfolio templates with the
 [PortfolioPrincipalAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html) resource.

Create End Users Policy and group:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-IAM-Endusers&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/iam/sc-enduser-iam.yml)  

Create All roles:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-IAM-AllRoles&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/iam/sc-launchrole-createall.json)  

Create EC2 and VPC roles:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-IAM-EC2VPCRoles&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/iam/sc-ec2vpc-launchrole.yml)  

Create S3 roles:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-IAM-S3Roles&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/iam/sc-s3-launchrole.yml)  

Create EMR roles:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-IAM-EMRRoles&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/iam/sc-emr-launchrole.yml)  

Create RDS roles:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-IAM-RDSRoles&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/iam/sc-rds-launchrole.yml)  

