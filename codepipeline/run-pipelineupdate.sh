#!/bin/bash
echo "Using Account:$ACCID  Region:$AWS_DEFAULT_REGION"
ACCID=$(aws sts get-caller-identity --query 'Account' | tr -d '"')
ESTR=$((aws cloudformation update-stack --stack-name SC-RA-IACPipeline --parameters '[{"ParameterKey":"ChildAccountAccess","UsePreviousValue":true}]' --template-url "https://s3.amazonaws.com/servicesatalog-deployedtemplates-$ACCID/codepipeline/sc-codepipeline-ra.json" --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND) 2>&1)
ECODE=$?
if [[ "$ECODE" -eq "255" && "$ESTR" =~ .(No updates are to be performed\.)$ ]]
then 
  echo "No updates, continue."
  exit 0
else
  echo "$ECODE $ESTR"
  exit $ECODE
fi