#!/bin/bash
echo "Using Account:$ACCID  Region:$AWS_DEFAULT_REGION"
NOUPDATES=false
ACCID=$(aws sts get-caller-identity --query 'Account' | tr -d '"')
ESTR=$((aws cloudformation update-stack --stack-name SC-IAC-automated-IAMroles  --parameters "[{\"ParameterKey\":\"RepoRootURL\",\"ParameterValue\":\"https://s3.amazonaws.com/servicesatalog-deployedtemplates-$ACCID/\"}]" --template-url "https://s3.amazonaws.com/servicesatalog-deployedtemplates-$ACCID/iam/sc-demosetup-iam.json" --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND) 2>&1)
ECODE=$?
if [[ "$ECODE" -eq "255" && "$ESTR" =~ .(No updates are to be performed\.)$ ]] ; then 
  NOUPDATES=true
fi

ESTR=$((aws cloudformation update-stack --stack-name SC-IAC-automated-portfolio --parameters "[{\"ParameterKey\":\"LinkedRole2\",\"UsePreviousValue\":true},{\"ParameterKey\":\"LinkedRole1\",\"UsePreviousValue\":true},{\"ParameterKey\":\"LaunchRoleName\",\"UsePreviousValue\":true},{\"ParameterKey\":\"RepoRootURL\",\"ParameterValue\":\"https://s3.amazonaws.com/servicesatalog-deployedtemplates-$ACCID/\"}]" --template-url "https://s3.amazonaws.com/servicesatalog-deployedtemplates-$ACCID/ec2/sc-portfolio-ec2demo.json") 2>&1)
ECODE=$?
if [[ "$ECODE" -eq "255" && "$ESTR" =~ .(No updates are to be performed\.)$ ]] ; then
  NOUPDATES=true
fi

if [ "$NOUPDATES" = true ]
then 
  echo "No updates, continue."
  exit 0
else
  echo "$ECODE $ESTR"
  exit $ECODE
fi