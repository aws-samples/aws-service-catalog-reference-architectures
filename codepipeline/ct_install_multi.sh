#!/bin/bash

# This script will setup the Automated pipeline, IAM Roles, and a ServiceCatalog Portfolio using the 
# reference architecture as example products.  This will create resources in your currently active CLI account
# across three regions using CloudFormation StackSets.  You will be responsible for any costs resulting from the usage
# of this script.

CreateEndUser=${1:-"Yes"}
CreateEndUsers=$(echo $CreateEndUser|tr '[:lower:]' '[:upper:]')
ACC=$(aws sts get-caller-identity --query 'Account' | tr -d '"')
# add child accounts as space delimited list. 
# You will need to ensure StackSet IAM roles are correctly setup in each child account
childAcc=""
childAccComma=${childAcc// /,}
allACC="$ACC $childAcc"
allACCCount=$(echo $allACC |wc -w)
allregions="us-east-1 us-east-2"
export AWS_DEFAULT_REGION=$(aws configure get region)
LinkedRole1=""
S3RootURL="https://s3.amazonaws.com/aws-service-catalog-reference-architectures"
SSTemplateURL="https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1"
SSAdminRoleStack="$SSTemplateURL/AWSCloudFormationStackSetAdministrationRole.yml"
SSExecRoleStack="$SSTemplateURL/AWSCloudFormationStackSetExecutionRole.yml"

CFTSSAdminRole="arn:aws:iam::${ACC}:role/service-role/AWSControlTowerStackSetRole"
CFTSSExecRole='AWSControlTowerExecution'

function check_stackset_status()
{
SSNAME=$1
SSROLEOPID=$2

STATUS=""
until [ "$STATUS" = "SUCCEEDED" ]; do 
STATUS=$(aws cloudformation describe-stack-set-operation --stack-set-name $SSNAME --operation-id $SSROLEOPID | jq '.StackSetOperation.Status' | tr -d '"')
echo "waiting for $SSNAME Stackset to complete. current status: $STATUS"
sleep 10
done
}

date


echo "Using Account:$ACC  Region:$AWS_DEFAULT_REGION Child Accounts:$childAcc All Regions:$allregions"

echo "creating the automation pipeline stack"
aws cloudformation create-stack --region $AWS_DEFAULT_REGION --stack-name SC-RA-IACPipeline --parameters "[{\"ParameterKey\":\"ChildAccountAccess\",\"ParameterValue\":\"$childAccComma\"}]" --template-url "$S3RootURL/codepipeline/sc-codepipeline-ra.json" --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND

echo "creating the ServiceCatalog IAM roles StackSet"
if [[ $CreateEndUsers == 'YES' || $CreateEndUsers == 'Y' ]]
then
        echo "Creating the StackSet IAM roles on Hub Account"
        aws cloudformation create-stack --stack-name IAM-StackSetAdministrator --template-url $SSAdminRoleStack --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
        aws cloudformation create-stack --stack-name IAM-StackSetExecution --parameters "[{\"ParameterKey\":\"AdministratorAccountId\",\"ParameterValue\":\"$ACC\"}]" --template-url $SSExecRoleStack --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
        echo "waiting for stacks to complete on Hub Account..."
        aws cloudformation wait stack-create-complete --stack-name IAM-StackSetAdministrator
        aws cloudformation wait stack-create-complete --stack-name IAM-StackSetExecution
        echo "Creating the cross-account IAM roles for Cloudformation StackSets ..."
        aws cloudformation create-stack-set --stack-set-name IAM-StackSetExecution-Role --parameters "[{\"ParameterKey\":\"AdministratorAccountId\",\"ParameterValue\":\"$ACC\"}]" --template-url $SSExecRoleStack --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND --administration-role-arn $CFTSSAdminRole --execution-role-name $CFTSSExecRole
        SSROLEOPID=$(aws cloudformation create-stack-instances --stack-set-name IAM-StackSetExecution-Role --regions $AWS_DEFAULT_REGION --accounts $childAcc --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=${allACCCount} | jq '.OperationId' | tr -d '"')
        check_stackset_status IAM-StackSetExecution-Role $SSROLEOPID
else
        echo "Skipping StackSet Roles, based of user selection...."
fi

echo "creating the ServiceCatalog IAM roles StackSet" 
aws cloudformation create-stack-set --stack-set-name SC-IAC-automated-IAMroles --template-url "$S3RootURL/iam/sc-demosetup-iam.json" --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
echo "Create IAM Roles on ${allACC}"
SSROLEOPID=$(aws cloudformation create-stack-instances --stack-set-name SC-IAC-automated-IAMroles --regions $AWS_DEFAULT_REGION --accounts $allACC --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=${allACCCount} | jq '.OperationId' | tr -d '"')

check_stackset_status SC-IAC-automated-IAMroles $SSROLEOPID

echo "creating the ServiceCatalog Portfolio StackSet"
aws cloudformation create-stack-set --stack-set-name SC-IAC-automated-portfolio --parameters "[{\"ParameterKey\":\"PorfolioName\",\"ParameterValue\":\"SC-RA\"},{\"ParameterKey\":\"LinkedRole1\",\"ParameterValue\":\"$LinkedRole1\"},{\"ParameterKey\":\"LinkedRole2\",\"ParameterValue\":\"\"},{\"ParameterKey\":\"LaunchRoleName\",\"ParameterValue\":\"SCEC2LaunchRole\"},{\"ParameterKey\":\"RepoRootURL\",\"ParameterValue\":\"$S3RootURL/\"},{\"ParameterKey\":\"CreateEndUsers\",\"ParameterValue\":\"No\"}]" --template-url "$S3RootURL/ec2/sc-portfolio-ec2demo.json" --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
SSROLEOPID=$(aws cloudformation create-stack-instances --stack-set-name SC-IAC-automated-portfolio --regions $allregions --accounts $allACC --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=${allACCCount} | jq '.OperationId' | tr -d '"')

check_stackset_status SC-IAC-automated-portfolio $SSROLEOPID

date
echo "Complete.  See CloudFormation Stacks and StackSets Console in each region for more details: $allregions"
