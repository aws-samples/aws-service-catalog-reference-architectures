#!/bin/bash
echo "You must provide your account id as the first argument"
aws s3 sync s3://aws-service-catalog-reference-architectures/ . --delete --exclude "*" --include "*.json" --include "*.yml"
echo "S3 download Complete, launching cloudformation now..."
aws cloudformation create-stack --stack-name SC-RA-IACPipeline https://s3.amazonaws.com/aws-service-catalog-reference-architectures/codepipeline/sc-codepipeline-ra.json
aws cloudformation create-stack-set --stack-set-name SC-IAC-automated-IAMroles --parameters '[{"ParameterKey":"RepoRootURL","ParameterValue":"https://s3.amazonaws.com/aws-service-catalog-reference-architectures/"}]' --template-url https://s3.amazonaws.com/aws-service-catalog-reference-architectures/iam/sc-ec2vpc-launchrole.json --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND                     
aws cloudformation create-stack-instances --stack-set-name SC-IAC-automated-IAMroles --regions '["us-east-1"]' --accounts '["$1"]' --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=2
aws cloudformation create-stack-set --stack-set-name SC-IAC-automated-portfolio --parameters '[{"ParameterKey":"LinkedRole1","ParameterValue":"Admin"},{"ParameterKey":"LinkedRole2","ParameterValue":""},{"ParameterKey":"LaunchRoleName","ParameterValue":"SCEC2LaunchRole"},{"ParameterKey":"RepoRootURL","ParameterValue":"https://s3.amazonaws.com/aws-service-catalog-reference-architectures/"}]' --template-url https://s3.amazonaws.com/aws-service-catalog-reference-architectures/ec2/sc-portfolio-ec2VPC.json 
aws cloudformation create-stack-instances --stack-set-name SC-IAC-automated-portfolio --regions '["us-east-1","us-east-2","us-west-1"]' --accounts '["$1"]' --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=2
