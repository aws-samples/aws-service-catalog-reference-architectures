#!/bin/bash

# This script will remove the Automated pipeline, IAM Roles, and a ServiceCatalog Portfolio created by the install.sh.  

ACC=$(aws sts get-caller-identity --query 'Account' | tr -d '"')
# add child accounts as space delimited list. 
# You will need to ensure StackSet IAM roles are correctly setup in each child account
childAcc=""
allACC="$ACC $childAcc"
allregions="us-east-1 us-east-2 us-west-1"
export AWS_DEFAULT_REGION=us-east-1
export AWS_DEFAULT_REGION=$(aws configure get region)
echo "Using Account:$ACC  Region:$AWS_DEFAULT_REGION Child Accounts:$childAcc All Regions:$allregions"

function delete_stack_set()
{
SSNAME=${1:-'None'}

SSaccList=$(aws cloudformation list-stack-instances --stack-set-name $SSNAME --query 'Summaries[*].Account' --output text | xargs -n1 | sort |uniq| xargs)
SSregList=$(aws cloudformation list-stack-instances --stack-set-name $SSNAME --query 'Summaries[*].Region' --output text | xargs -n1 | sort |uniq| xargs)

echo "$SSaccList, $SSregList"

echo "aws cloudformation delete-stack-instances --stack-set-name $SSNAME --accounts $SSaccList --regions $SSregList --operation-preferences FailureToleranceCount=1,MaxConcurrentCount=3 --no-retain-stacks --query 'OperationId' --output text"
SSOPID=$(aws cloudformation delete-stack-instances --stack-set-name $SSNAME --accounts $SSaccList --regions $SSregList --operation-preferences FailureToleranceCount=1,MaxConcurrentCount=3 --no-retain-stacks --query 'OperationId' --output text)

echo $SSOPID

wait_for_deletion $SSNAME $SSOPID

aws cloudformation delete-stack-set --stack-set-name $SSNAME

}

function wait_for_deletion()
{
SSNAME=${1:-SC-IAC-automated-portfolio}
SSOPID=$2

STATUS=""
until [ "$STATUS" = "SUCCEEDED" ]; do 
  STATUS=$(aws cloudformation describe-stack-set-operation --stack-set-name $SSNAME --operation-id $SSOPID --query 'StackSetOperation.Status' --output text)
  echo "waiting for portfolio Stackset to delete. current status: $STATUS"
  sleep 5
done;
}

function clean_s3_buckets()
{
SNAME=${1:-SC-RA-IACPipeline}
for BNAME in $(aws cloudformation list-stack-resources --stack-name SC-RA-IACPipeline --query 'StackResourceSummaries[?ResourceType==`AWS::S3::Bucket`].PhysicalResourceId' --output text | xargs -n1)
do
aws s3 rb s3://$BNAME --force
done
}

function delete_stacks()
{
SNAME=${1:-RSC-RA-IACPipeline}
echo "Deleting the automated pipeline stack."
aws cloudformation delete-stack --stack-name $SNAME
echo "Waiting for Stack deletion to complete"
aws cloudformation wait stack-create-complete --stack-name $SNAME
}

# multi account multi region, CF StackSet
echo "Deleting the ServiceCatalog Portfolio StackSet, this make take a while."
delete_stack_set SC-IAC-automated-portfolio
delete_stack_set SC-IAC-automated-IAMroles
delete_stack_set IAM-StackSetExecution-Role

echo "Clearing out the Automation pipeline S3 buckets"
clean_s3_buckets SC-RA-IACPipeline

echo "Deleting the automated pipeline stack."
delete_stacks SC-RA-IACPipeline

echo "Deleting the StackSet IAM roles."
delete_stacks IAM-StackSetAdministrator
delete_stacks IAM-StackSetExecution

echo "Cleanup process completed... "
