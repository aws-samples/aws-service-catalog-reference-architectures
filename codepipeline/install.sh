#!/bin/bash

# This script will setup the Automated pipeline, IAM Roles, and a ServiceCatalog Portfolio using the 
# reference architecture as example products.  This will create resources in your currently active CLI account
# across three regions using CloudFormation StackSets.  You will be responsible for any costs resulting from the usage
# of this script.

ACC=$(aws sts get-caller-identity --query 'Account' | tr -d '"')
# add child accounts as space delimited list. 
# You will need to ensure StackSet IAM roles are correctly setup in each child account
childAcc=""
childAccComma=${childAcc// /,}
allACC="$ACC $childAcc"
export AWS_DEFAULT_REGION=us-east-1
allregions="us-east-1 us-east-2 us-west-1"
LinkedRole1=""
S3RootURL="https://s3.amazonaws.com/aws-service-catalog-reference-architectures"

date
echo "Using Account:$ACC  Region:$AWS_DEFAULT_REGION Child Accounts:$childAcc All Regions:$allregions"

echo "Creating the StackSet IAM roles"
aws cloudformation create-stack --region $AWS_DEFAULT_REGION --stack-name IAM-StackSetAdministrator --template-url https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AWSCloudFormationStackSetAdministrationRole.yml --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
aws cloudformation create-stack --region $AWS_DEFAULT_REGION --stack-name IAM-StackSetExecution --parameters "[{\"ParameterKey\":\"AdministratorAccountId\",\"ParameterValue\":\"$ACC\"}]" --template-url https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AWSCloudFormationStackSetExecutionRole.yml --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
echo "waiting for stacks to complete..."
aws cloudformation wait stack-create-complete --stack-name IAM-StackSetAdministrator
aws cloudformation wait stack-create-complete --stack-name IAM-StackSetExecution

echo "creating the automation pipeline stack"
aws cloudformation create-stack --region $AWS_DEFAULT_REGION --stack-name SC-RA-IACPipeline --parameters "[{\"ParameterKey\":\"ChildAccountAccess\",\"ParameterValue\":\"$childAccComma\"}]" --template-url "$S3RootURL/codepipeline/sc-codepipeline-ra.json" --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND

echo "creating the ServiceCatalog IAM roles StackSet"
aws cloudformation create-stack-set --stack-set-name SC-IAC-automated-IAMroles --template-url "$S3RootURL/iam/sc-demosetup-iam.json" --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
SSROLEOPID=$(aws cloudformation create-stack-instances --stack-set-name SC-IAC-automated-IAMroles --regions $AWS_DEFAULT_REGION --accounts $allACC --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=1 | jq '.OperationId' | tr -d '"')
STATUS=""
until [ "$STATUS" = "SUCCEEDED" ]; do 
  STATUS=$(aws cloudformation describe-stack-set-operation --stack-set-name SC-IAC-automated-IAMroles --operation-id $SSROLEOPID | jq '.StackSetOperation.Status' | tr -d '"')
  echo "waiting for IAMrole Stackset to complete. current status: $STATUS"
  sleep 10
done

echo "creating the ServiceCatalog Portfolio StackSet"
aws cloudformation create-stack-set --stack-set-name SC-IAC-automated-portfolio --parameters "[{\"ParameterKey\":\"LinkedRole1\",\"ParameterValue\":\"$LinkedRole1\"},{\"ParameterKey\":\"LinkedRole2\",\"ParameterValue\":\"\"},{\"ParameterKey\":\"LaunchRoleName\",\"ParameterValue\":\"SCEC2LaunchRole\"},{\"ParameterKey\":\"RepoRootURL\",\"ParameterValue\":\"$S3RootURL/\"}]" --template-url "$S3RootURL/ec2/sc-portfolio-ec2demo.json" --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation create-stack-instances --stack-set-name SC-IAC-automated-portfolio --regions $allregions --accounts $ACC --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=3

date
echo "Complete.  See CloudFormation Stacks and StackSets Console in each region for more details: $allregions"
