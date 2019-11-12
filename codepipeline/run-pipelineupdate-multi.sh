#!/bin/bash
echo "Using Account:$ACCID  Region:$AWS_DEFAULT_REGION"
ACCID=$(aws sts get-caller-identity --query 'Account' | tr -d '"')
ALIAS=initial
StackName=${ALIAS}-SC-RA-IACPipeline
S3Https=https://s3.amazonaws.com/servicesatalog-deployedtemplates-${ACCID}-${ALIAS}
ESTR=$((aws cloudformation update-stack --stack-name $StackName --parameters '[{"ParameterKey":"ChildAccountAccess","UsePreviousValue":true},{"ParameterKey":"RandomString","UsePreviousValue":true}]' --template-url "${S3Https}/codepipeline/sc-codepipeline-ra-ct-multi.json" --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND) 2>&1)
ECODE=$?
if [[ "$ECODE" -eq "255" && "$ESTR" =~ .(No updates are to be performed\.)$ ]]
then 
  echo "No updates, continue."
  exit 0
else
  echo "$ECODE $ESTR"
  exit $ECODE
fi
