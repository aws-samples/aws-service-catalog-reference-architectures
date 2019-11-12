#!/bin/bash

# This script will setup the Automated pipeline, IAM Roles, and a ServiceCatalog Portfolio using the 
# reference architecture as example products.  This will create resources in your currently active CLI account
# across three regions using CloudFormation StackSets.  You will be responsible for any costs resulting from the usage
# of this script.

ALIASA=${1:-$((RANDOM*23))}
#ALIASA=${1:-$(head /dev/urandom | tr -dc A-Za-z | head -c 8)}
CreateEndUser=${2:-"No"}
ALIAS=$(echo $ALIASA|tr [0-9] [a-z]|tr '[:upper:]' '[:lower:]')
CreateEndUsers=$(echo $CreateEndUser|tr '[:lower:]' '[:upper:]')
ACC=$(aws sts get-caller-identity --query 'Account' | tr -d '"')
# add child accounts as space delimited list. 
# You will need to ensure StackSet IAM roles are correctly setup in each child account
childAcc="394149256169"
childAccComma=${childAcc// /,}
allACC="$ACC $childAcc"
allregions="us-east-1 us-east-2"
LinkedRole1=""
S3RootURL="https://s3.amazonaws.com/aws-service-catalog-reference-architectures"
CFTSSAdminRole="arn:aws:iam::${ACC}:role/service-role/AWSControlTowerStackSetRole"
CFTSSExecRole='AWSControlTowerExecution'

date
export AWS_DEFAULT_REGION=us-east-1
echo "Using Account:$ACC  Region:$AWS_DEFAULT_REGION Child Accounts:$childAcc All Regions:$allregions"

echo "creating the automation pipeline stack"
aws cloudformation create-stack --region us-east-1 --stack-name ${ALIAS}-SC-RA-IACPipeline --parameters "[{\"ParameterKey\":\"ChildAccountAccess\",\"ParameterValue\":\"$childAccComma\"},{\"ParameterKey\":\"CodeCommitRepoName\",\"ParameterValue\":\"${ALIAS}-SCPortfoliosRepo\"},{\"ParameterKey\":\"RandomString\",\"ParameterValue\":\"$ALIAS\"}]" --template-url "$S3RootURL/codepipeline/sc-codepipeline-ra-ct-multi.json" --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND

echo "creating the ServiceCatalog IAM roles StackSet"
if [[ $CreateEndUsers == 'YES' || $CreateEndUsers == 'Y' ]]
then
listACC=$allACC
else
listACC=$childAcc
fi

echo "Create IAM Roles on ${listACC}"
aws cloudformation create-stack-set --stack-set-name ${ALIAS}-SC-IAC-automated-IAMroles --parameters "[{\"ParameterKey\":\"RepoRootURL\",\"ParameterValue\":\"$S3RootURL/\"}]" --template-url "$S3RootURL/iam/sc-demosetup-iam.json" --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND --administration-role-arn $CFTSSAdminRole --execution-role-name $CFTSSExecRole
SSROLEOPID=$(aws cloudformation create-stack-instances --stack-set-name ${ALIAS}-SC-IAC-automated-IAMroles --regions $AWS_DEFAULT_REGION --accounts $listACC --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=1 | jq '.OperationId' | tr -d '"')
STATUS=""
until [ "$STATUS" = "SUCCEEDED" ]; do 
STATUS=$(aws cloudformation describe-stack-set-operation --stack-set-name ${ALIAS}-SC-IAC-automated-IAMroles --operation-id $SSROLEOPID | jq '.StackSetOperation.Status' | tr -d '"')
echo "waiting for IAMrole Stackset to complete. current status: $STATUS"
sleep 10
done

echo "creating the ServiceCatalog Portfolio StackSet"
aws cloudformation create-stack-set --stack-set-name ${ALIAS}-SC-IAC-automated-portfolio --parameters "[{\"ParameterKey\":\"PorfolioName\",\"ParameterValue\":\"${ALIAS}-SC-RA\"},{\"ParameterKey\":\"LinkedRole1\",\"ParameterValue\":\"$LinkedRole1\"},{\"ParameterKey\":\"LinkedRole2\",\"ParameterValue\":\"\"},{\"ParameterKey\":\"LaunchRoleName\",\"ParameterValue\":\"SCEC2LaunchRole\"},{\"ParameterKey\":\"RepoRootURL\",\"ParameterValue\":\"$S3RootURL/\"}]" --template-url "$S3RootURL/ec2/sc-portfolio-ec2VPC.json" --administration-role-arn $CFTSSAdminRole --execution-role-name $CFTSSExecRole --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation create-stack-instances --stack-set-name ${ALIAS}-SC-IAC-automated-portfolio --regions $allregions --accounts $allACC --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=3

date
echo "Complete.  See CloudFormation Stacks and StackSets Console in each region for more details: $allregions"
