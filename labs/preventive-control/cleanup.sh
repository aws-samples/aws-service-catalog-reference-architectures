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

# list of product to delete from Service Catalog
products_to_deploy=(sns elasticsearch ebs autoscaling alb albtarget alblistener s3)
# Domain Name to remove from ACM
domainName='www.example.com'

printf "Delete SSL Certificate from ACM\n"
certArn=$(aws acm list-certificates --query 'CertificateSummaryList[?DomainName==`'$domainName'`].CertificateArn' --output text)
aws acm delete-certificate --certificate-arn $certArn

# Delete Service Catalog Products
for i in ${products_to_deploy[*]}
do
  printf "Deleting Product: $i\n"
  aws cloudformation update-termination-protection --no-enable-termination-protection --stack-name "sc-$i-product-cfn"
  aws cloudformation delete-stack --stack-name "sc-$i-product-cfn"
done
