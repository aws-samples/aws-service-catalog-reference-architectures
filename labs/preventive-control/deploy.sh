#!/bin/bash

# /*
# * Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# *
# * Permission is hereby granted, free of charge, to any person obtaining a copy of this
# * software and associated documentation files (the "Software"), to deal in the Software
# * without restriction, including without limitation the rights to use, copy, modify,
# * merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# * permit persons to whom the Software is furnished to do so.
# *
# * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# * INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# * PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# */

# Domain Name of SSL Cert import to ACM
domain_name="www.example.com"
# list of product to deploy to Service Catalog
products_to_deploy=(sns elasticsearch ebs autoscaling alb albtarget alblistener s3 firehose)

# Variable and function to validate if products were deploy to AWS Service Catalog
deploymentStarted=false
deploymentFinished=true

no_cert=true

# optional AWS CLI profile. If not provided default profile will be used.
aws_cli_profile="default"


while [ "$1" != "" ]; do
    case $1 in
        nocert )
        no_cert=false
        shift
        ;;

        * )
        aws_cli_profile=$1
        shift
        ;;
    esac
done

printf "Deploying under AWS CLI Profile: $aws_cli_profile\n"

validate_products_deployment()
{
  for i in ${products_to_deploy[*]}
  do
    cfStat=$(aws cloudformation describe-stacks --stack-name "sc-$i-product-cfn" --query 'Stacks[].StackStatus' --region us-east-1 --profile $aws_cli_profile --output text 2> /dev/null)
    if [[ $cfStat != "" ]]
    then
      deploymentStarted=true
      if [ $cfStat != "CREATE_COMPLETE" ]
      then
        deploymentFinished=false
      fi
    fi
  done
}

printf "Read Deployment Variables\n"
# Get Resources Deployment CFN STack Name
resources_cfn_stack_name=$(aws cloudformation describe-stacks --query 'Stacks[?Tags[?Key==`LAB:Object` && Value==`sc-lab-resource-cfn`][]].StackName' --region us-east-1 --profile $aws_cli_profile --output text)
# Get Deployment S3 Bucket name
deployment_s3_bucket_name=$(aws cloudformation describe-stacks --query 'Stacks[?Tags[?Key==`LAB:Object` && Value==`sc-lab-lambdas-cfn`][]].Outputs[]' --region us-east-1 --profile $aws_cli_profile --output json | jq --raw-output '.[] | select(.OutputKey == "BucketName").OutputValue')
# Get Service Catalog IAM policy name
sc_product_policy_name=$(aws cloudformation describe-stacks --query 'Stacks[?Tags[?Key==`LAB:Object` && Value==`sc-lab-resource-cfn`][]].Parameters[]' --region us-east-1 --profile $aws_cli_profile --output json | jq --raw-output '.[] | select(.ParameterKey == "PolicyName").ParameterValue')

printf "Creating Service Linked Role"
aws iam create-service-linked-role --aws-service-name autoscaling.amazonaws.com --profile $aws_cli_profile
aws iam create-service-linked-role --aws-service-name elasticloadbalancing.amazonaws.com --profile $aws_cli_profile

if [ $no_cert = true ]
then
  printf "Generate and Import Self-Sign SSL Certificate to ACM\n"
  openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout certificate.key -out certificate.crt -subj "/C=US/ST=MA/L=Boston/O=Company/OU=IT/CN=$domain_name"
  certArn=$(aws acm import-certificate --certificate file://./certificate.crt --private-key file://./certificate.key --query 'CertificateArn' --region us-east-1 --profile $aws_cli_profile --output text)
  aws acm add-tags-to-certificate --certificate-arn $certArn --tags Key=Name,Value=sc-lab Key=Env,Value=lab --region us-east-1 --profile $aws_cli_profile
fi

printf "Download Deployment Configuration Files\n"
mkdir products-config
cd products-config/
for f in ${products_to_deploy[*]}
do
  printf "Downloading Configuration for Product: $f\n"
  wget -q https://s3.amazonaws.com/aws-service-catalog-reference-architectures/labs/preventive-control/products-config/sc-product-$f.deployer -O sc-product-$f.deployer
done
cd ..

sleep 30

getOS=$(uname -s)
for i in ${products_to_deploy[*]}
do
  printf "Deploying Configuration for Product: $i\n"

  if [ $getOS = "Darwin" ]
  then
    sed -i '' 's/var.deploymentBucket/'$deployment_s3_bucket_name'/g' products-config/sc-product-$i.deployer
    sed -i '' 's/var.portfolioCfn/'$resources_cfn_stack_name'/g' products-config/sc-product-$i.deployer
    sed -i '' 's/var.policy/'$sc_product_policy_name'/g' products-config/sc-product-$i.deployer
  else
    sed -i 's/var.deploymentBucket/'$deployment_s3_bucket_name'/g' products-config/sc-product-$i.deployer
    sed -i 's/var.portfolioCfn/'$resources_cfn_stack_name'/g' products-config/sc-product-$i.deployer
    sed -i 's/var.policy/'$sc_product_policy_name'/g' products-config/sc-product-$i.deployer
  fi
  aws s3 cp products-config/sc-product-$i.deployer s3://$deployment_s3_bucket_name/deployment-cfg/sc-product-$i.deployer --profile $aws_cli_profile
done

printf "Waiting for Products to be deploy ...\n"
sleep 60

printf "Validate Products deployment...\n"
statCount=0
while [ $deploymentStarted = false ]
do
  validate_products_deployment
  if [ $deploymentStarted = true ]
  then
    printf "Waiting for CF Stack to Finish ..."
    while [ $deploymentFinished = false ]
    do
      sleep 15
      printf "."
      validate_products_deployment
    done
  else
    if [ $statCount -eq 1 ]
    then
      printf "\nDeployment Failed. Please try to redeploy products by calling: \n ./deploy.sh nocert \n"
      exit 1
    fi
    sleep 60
    statCount=1
  fi
done

printf "\nDeployment Completed\n"
