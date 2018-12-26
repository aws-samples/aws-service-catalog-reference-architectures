#!/bin/bash
ACC=$(aws sts get-caller-identity --query 'Account' | tr -d '"')
export AWS_DEFAULT_REGION=us-east-1
echo "Using Account:$ACC  Region:$AWS_DEFAULT_REGION"

aws s3 rb s3://servicesatalog-pipelineartifacts-$ACC --force
aws s3 rb s3://servicesatalog-deployedtemplates-$ACC --force
aws s3 rb s3://taskcat-tempbucket-$ACC --force

# multi account multi region, CF StackSet
aws cloudformation delete-stack-instances --stack-set-name SC-IAC-automated-IAMroles --accounts $ACC --regions '["us-east-1"]' --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=1 --no-retain-stacks
aws cloudformation delete-stack-instances --stack-set-name SC-IAC-automated-portfolio --accounts $ACC --regions '["us-east-1","us-east-2","us-west-1"]' --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=1 --no-retain-stacks
aws cloudformation delete-stack-set --stack-set-name SC-IAC-automated-IAMroles 
aws cloudformation delete-stack-set --stack-set-name SC-IAC-automated-portfolio

# single account single region, regular CF stack
#aws cloudformation delete-stack --stack-name SC-IAC-automated-IAMroles 
#aws cloudformation delete-stack --stack-name SC-IAC-automated-portfolio


aws cloudformation delete-stack --region us-east-1 --stack-name SC-RA-IACPipeline
 