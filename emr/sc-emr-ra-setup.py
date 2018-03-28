#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
  Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
  
  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at
  
      http://www.apache.org/licenses/LICENSE-2.0
  
  or in the "license" file accompanying this file. This file is distributed 
  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
  express or implied. See the License for the specific language governing 
  permissions and limitations under the License.
"""

import boto3
import random

#####
# *** NOTE ***
# please note that I am not setting the AWS region in this code 
# which means that it will default to the AWS region of the shell 
# where the run this script from.  The region can be specified 
# in the client call by setting the region_name parameter/value 
# to the appropriate AWS region
#####

#####
# Psuedo Code
# 1 - Create portfolio 
# 2 - Create product within service catalog
# 3 - Add product to portfolio
# 4 - Return details back to user
#####


#####
# GLOBAL PARAMETERS
#####
product_owner='IT Services'
product_distributor='IT Services'
support_description='Operations Team'
support_email='support@yourcompany.com'
support_url='http://helpdesk.yourcompany.com'
product_type='CLOUD_FORMATION_TEMPLATE'


#####
# Start Service Catalog BOTO3 API Client
#####
client = boto3.client('servicecatalog')
print('STARTED -- Setup of Service Catalog EMR Reference Architecture.')
print('')

#####
# Create Portfolio
#####
token = "token"+str(int(random.random()*8675309))
response = client.create_portfolio(
    AcceptLanguage='en',
    DisplayName='Service Catalog EMR Reference Architecture',
    Description='Service Catalog Portfolio that contains reference architecture products for Amazon Elastic MapReduce (EMR).',
    ProviderName=product_owner,
    Tags=[
        {
            'Key': 'Portfolio',
            'Value': 'Service Catalog EMR Reference Architecture'
        }
    ],
    IdempotencyToken=token
)
portfolio_id = response['PortfolioDetail']['Id']
portfolio_arn = response['PortfolioDetail']['ARN']
print("PORTFOLIO CREATED: Service Catalog EMR Reference Architecture")
print("--id=" + portfolio_id)
print("--arn=" + portfolio_arn)
print('')


#####
# Create Product: EMR
#####
token = "token"+str(int(random.random()*8765309))
response = client.create_product(
    AcceptLanguage='en',
    Name='Amazon Elastic MapReduce (EMR)',
    Description='This product builds an Amazon Elastic MapReduce cluster with 1 master nodes and 2 core nodes.',
    Owner=product_owner,
    Distributor=product_distributor,
    SupportDescription=support_description,
    SupportEmail=support_email,
    SupportUrl=support_url,
    ProductType=product_type,
    Tags=[
        {
            'Key': 'ProductType',
            'Value': 'AWS EMR'
        }
    ],
    ProvisioningArtifactParameters={
        'Name': 'v1.0',
        'Description': 'baseline version',
        'Info': {
            "LoadTemplateFromURL" : "https://s3.us-east-2.amazonaws.com/islawson-service-catalog-reference-architecture/emr/sc-emr-ra.json"
        },
        'Type': 'CLOUD_FORMATION_TEMPLATE'
    },
    IdempotencyToken=token
)
emr_product_id = response['ProductViewDetail']['ProductViewSummary']['ProductId']
print("PRODUCT CREATED: Amazon Elastic MapReduce (EMR)")


#####
# Associate EMR Product with Portfolio
#####
response = client.associate_product_with_portfolio(
    AcceptLanguage='en',
    ProductId=emr_product_id,
    PortfolioId=portfolio_id,
)
print("PRODUCT/PORTFOLIO ASSOCIATED: AWS EMR")
print("--id=" + emr_product_id)
print('')


#####
# End Process
#####
print("FINISHED -- Setup of Service Catalog EMR Reference Architecture.")
print('')