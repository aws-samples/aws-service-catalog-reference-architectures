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
print('STARTED -- Setup of Service Catalog EC2 Reference Architecture.')
print('')

#####
# Create Portfolio
#####
token = "token"+str(int(random.random()*8675309))
response = client.create_portfolio(
    AcceptLanguage='en',
    DisplayName='Service Catalog EC2 Reference Architecture',
    Description='Service Catalog Portfolio that contains reference architecture products for Amazon Elastic Compute Cloud (EC2).',
    ProviderName=product_owner,
    Tags=[
        {
            'Key': 'Portfolio',
            'Value': 'Service Catalog EC2 Reference Architecture'
        }
    ],
    IdempotencyToken=token
)
portfolio_id = response['PortfolioDetail']['Id']
portfolio_arn = response['PortfolioDetail']['ARN']
print("PORTFOLIO CREATED: Service Catalog EC2 Reference Architecture")
print("--id=" + portfolio_id)
print("--arn=" + portfolio_arn)
print('')


#####
# Create Product: EC2 Linux Instance
#####
token = "token"+str(int(random.random()*8765309))
response = client.create_product(
    AcceptLanguage='en',
    Name='Amazon Elastic Compute Cloud (EC2) Linux',
    Description='This product builds one Amazon Linux EC2 instance and create a SSM patch baseline, maintenance window, and patch task to scan for and install operating system updates the EC2 instance.',
    Owner=product_owner,
    Distributor=product_distributor,
    SupportDescription=support_description,
    SupportEmail=support_email,
    SupportUrl=support_url,
    ProductType=product_type,
    Tags=[
        {
            'Key': 'ProductType',
            'Value': 'AWS EC2 Linux'
        }
    ],
    ProvisioningArtifactParameters={
        'Name': 'v1.0',
        'Description': 'baseline version',
        'Info': {
            "LoadTemplateFromURL" : "https://raw.githubusercontent.com/aws-samples/aws-service-catalog-reference-architectures/master/ec2/sc-ec2-linux-ra.json"
        },
        'Type': 'CLOUD_FORMATION_TEMPLATE'
    },
    IdempotencyToken=token
)
ec2_linux_product_id = response['ProductViewDetail']['ProductViewSummary']['ProductId']
print("PRODUCT CREATED: Amazon Elastic Compute Cloud (EC2) Linux")


#####
# Associate EC2 Linux Product with Portfolio
#####
response = client.associate_product_with_portfolio(
    AcceptLanguage='en',
    ProductId=ec2_linux_product_id,
    PortfolioId=portfolio_id,
)
print("PRODUCT/PORTFOLIO ASSOCIATED: AWS EC2 Linux")
print("--id=" + ec2_linux_product_id)
print('')

#####
# Create Product: EC2 Windows
#####
token = "token"+str(int(random.random()*8765309))
response = client.create_product(
    AcceptLanguage='en',
    Name='Amazon Elastic Compute Cloud (EC2) Windows',
    Description='This product builds one Microsoft Windows EC2 instance and create a SSM patch baseline, maintenance window, and patch task to scan for and install operating system updates on the EC2 instance.',
    Owner=product_owner,
    Distributor=product_distributor,
    SupportDescription=support_description,
    SupportEmail=support_email,
    SupportUrl=support_url,
    ProductType=product_type,
    Tags=[
        {
            'Key': 'ProductType',
            'Value': 'AWS EC2 Windows'
        }
    ],
    ProvisioningArtifactParameters={
        'Name': 'v1.0',
        'Description': 'baseline version',
        'Info': {
            "LoadTemplateFromURL" : "https://github.com/aws-samples/aws-service-catalog-reference-architectures/blob/master/ec2/sc-ec2-windows-ra.json"
        },
        'Type': 'CLOUD_FORMATION_TEMPLATE'
    },
    IdempotencyToken=token
)
ec2_windows_product_id = response['ProductViewDetail']['ProductViewSummary']['ProductId']
print("PRODUCT CREATED: Amazon Elastic Compute Cloud (EC2) Windows")


#####
# Associate EC2 Windows Product with Portfolio
#####
response = client.associate_product_with_portfolio(
    AcceptLanguage='en',
    ProductId=ec2_windows_product_id,
    PortfolioId=portfolio_id,
)
print("PRODUCT/PORTFOLIO ASSOCIATED: AWS EC2")
print("--id=" + ec2_windows_product_id)
print('')


#####
# End Process
#####
print("FINISHED -- Setup of Service Catalog EC2 Reference Architecture.")
print('')