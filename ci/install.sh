#!/bin/bash
ACC=$(aws sts get-caller-identity --query 'Account' | tr -d '"')
export AWS_DEFAULT_REGION=us-east-1
echo "Using Account:$ACC  Region:$AWS_DEFAULT_REGION"

#create the automation pipeline
aws cloudformation create-stack --stack-name SC-RA-IACPipeline --parameters '[{"ParameterKey":"ChildAccountAccess","ParameterValue":""}]' --template-url https://s3.amazonaws.com/aws-service-catalog-reference-architectures/codepipeline/sc-codepipeline-ra.json --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND

# multi account multi region, CF StackSet
aws cloudformation create-stack-set --stack-set-name SC-IAC-automated-IAMroles --parameters '[{"ParameterKey":"RepoRootURL","ParameterValue":"https://s3.amazonaws.com/aws-service-catalog-reference-architectures/"}]' --template-url https://s3.amazonaws.com/aws-service-catalog-reference-architectures/iam/sc-ec2vpc-launchrole.yml --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation create-stack-set --stack-set-name SC-IAC-automated-portfolio --parameters '[{"ParameterKey":"LinkedRole1","ParameterValue":"Admin"},{"ParameterKey":"LinkedRole2","ParameterValue":""},{"ParameterKey":"LaunchRoleName","ParameterValue":"SCEC2LaunchRole"},{"ParameterKey":"RepoRootURL","ParameterValue":"https://s3.amazonaws.com/aws-service-catalog-reference-architectures/"}]' --template-url https://s3.amazonaws.com/aws-service-catalog-reference-architectures/ec2/sc-portfolio-ec2VPC.json 
#aws cloudformation create-stack-instances --stack-set-name SC-IAC-automated-IAMroles --regions '["us-east-1"]' --accounts $ACC --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=2
#aws cloudformation create-stack-instances --stack-set-name SC-IAC-automated-portfolio --regions '["us-east-1","us-east-2","us-west-1"]' --accounts $ACC --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=2

# single account single region, regular CF stack
#aws cloudformation create-stack --stack-name SC-IAC-automated-IAMroles --template-url https://s3.amazonaws.com/aws-service-catalog-reference-architectures/iam/sc-ec2vpc-launchrole.yml --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
#aws cloudformation create-stack --stack-name SC-IAC-automated-portfolio --parameters '[{"ParameterKey":"LinkedRole1","ParameterValue":"Admin"},{"ParameterKey":"LinkedRole2","ParameterValue":""},{"ParameterKey":"LaunchRoleName","ParameterValue":"SCEC2LaunchRole"},{"ParameterKey":"RepoRootURL","ParameterValue":"https://s3.amazonaws.com/aws-service-catalog-reference-architectures/"}]' --template-url https://s3.amazonaws.com/aws-service-catalog-reference-architectures/ec2/sc-portfolio-ec2VPC.json 

