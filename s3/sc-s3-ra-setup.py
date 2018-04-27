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
print ("STARTED -- Setup of Service Catalog S3 Reference Architecture.")
print ("")

#####
# Create Portfolio
#####
token = "token"+str(int(random.random()*8675309))
response = client.create_portfolio(
    AcceptLanguage='en',
    DisplayName='Service Catalog S3 Reference Architecture',
    Description='Service Catalog Portfolio that contains reference architecture products for Amazon Simple Storage Service.',
    ProviderName=product_owner,
    Tags=[
        {
            'Key': 'Portfolio',
            'Value': 'Service Catalog S3 Reference Architecture'
        }
    ],
    IdempotencyToken=token
)
portfolio_id = response['PortfolioDetail']['Id']
portfolio_arn = response['PortfolioDetail']['ARN']
print ("PORTFOLIO CREATED: Service Catalog S3 Reference Architecture")
print ("--id=" + portfolio_id)
print ("--arn=" + portfolio_arn)
print ("")


#####
# Create Product: S3 Public Access Read Only Bucket
#####
token = "token"+str(int(random.random()*8765309))
response = client.create_product(
    AcceptLanguage='en',
    Name='Amazon S3 Public Bucket with Read Only Access',
    Description='This product builds an Amazon AWS S3 bucket with options for read only bucket with public access from any source.',
    Owner=product_owner,
    Distributor=product_distributor,
    SupportDescription=support_description,
    SupportEmail=support_email,
    SupportUrl=support_url,
    ProductType=product_type,
    Tags=[
        {
            'Key': 'ProductType',
            'Value': 'Amazon S3 Public Bucket with Read Only Access'
        }
    ],
    ProvisioningArtifactParameters={
        'Name': 'v1.0',
        'Description': 'baseline version',
        'Info': {
            "LoadTemplateFromURL" : "https://raw.githubusercontent.com/aws-samples/aws-service-catalog-reference-architectures/master/s3/sc-s3-public-ra.json"
        },
        'Type': 'CLOUD_FORMATION_TEMPLATE'
    },
    IdempotencyToken=token
)
s3_public_bucket_product_id = response['ProductViewDetail']['ProductViewSummary']['ProductId']
print ("PRODUCT CREATED: Amazon S3 Public Bucket with Read Only Access")


#####
# Associate S3 Public Access Read Only Bucket 
#####
response = client.associate_product_with_portfolio(
    AcceptLanguage='en',
    ProductId=s3_public_bucket_product_id,
    PortfolioId=portfolio_id,
)
print ("PRODUCT/PORTFOLIO ASSOCIATED: Amazon S3 Public Access Read Only Bucket")
print ("--id=" + s3_public_bucket_product_id)
print ("")


#####
# Create Product: S3 Private Access Restricted Source Bucket
#####
token = "token"+str(int(random.random()*8765309))
response = client.create_product(
    AcceptLanguage='en',
    Name='Amazon S3 Private Bucket with CIDR Restricted Access',
    Description='This product builds an Amazon AWS S3 bucket with private access accessible from a restricted soure.',
    Owner=product_owner,
    Distributor=product_distributor,
    SupportDescription=support_description,
    SupportEmail=support_email,
    SupportUrl=support_url,
    ProductType=product_type,
    Tags=[
        {
            'Key': 'ProductType',
            'Value': 'Amazon S3 Private Bucket with CIDR Restricted Access'
        }
    ],
    ProvisioningArtifactParameters={
        'Name': 'v1.0',
        'Description': 'baseline version',
        'Info': {
            "LoadTemplateFromURL" : "https://raw.githubusercontent.com/aws-samples/aws-service-catalog-reference-architectures/master/s3/sc-s3-cidr-ra.json"
        },
        'Type': 'CLOUD_FORMATION_TEMPLATE'
    },
    IdempotencyToken=token
)
s3_cidr_bucket_product_id = response['ProductViewDetail']['ProductViewSummary']['ProductId']
print ("PRODUCT CREATED: Amazon S3 Private Bucket with CIDR Restricted Access")


#####
# Associate S3 MySQL Product with Portfolio
#####
response = client.associate_product_with_portfolio(
    AcceptLanguage='en',
    ProductId=s3_cidr_bucket_product_id,
    PortfolioId=portfolio_id,
)
print ("PRODUCT/PORTFOLIO ASSOCIATED: Amazon S3 Private Bucket with CIDR Restricted Access")
print ("--id=" + s3_cidr_bucket_product_id)
print ("")


#####
# Create Product: Amazon S3 Private Encrypted Bucket
#####
token = "token"+str(int(random.random()*8765309))
response = client.create_product(
    AcceptLanguage='en',
    Name='Amazon S3 Private Encrypted Bucket',
    Description='This product builds an Amazon AWS S3 bucket encrypted with private access accessible from any source.',
    Owner=product_owner,
    Distributor=product_distributor,
    SupportDescription=support_description,
    SupportEmail=support_email,
    SupportUrl=support_url,
    ProductType=product_type,
    Tags=[
        {
            'Key': 'ProductType',
            'Value': 'Amazon S3 Private Encrypted Bucket'
        }
    ],
    ProvisioningArtifactParameters={
        'Name': 'v1.0',
        'Description': 'baseline version',
        'Info': {
            "LoadTemplateFromURL" : "https://raw.githubusercontent.com/aws-samples/aws-service-catalog-reference-architectures/master/s3/sc-s3-encrypted-ra.json"
        },
        'Type': 'CLOUD_FORMATION_TEMPLATE'
    },
    IdempotencyToken=token
)
s3_encrypted_bucket_product_id = response['ProductViewDetail']['ProductViewSummary']['ProductId']
print ("PRODUCT CREATED: Amazon S3 Private Encrypted Bucket")


#####
# Associate Amazon S3 Encrypted Bucket
#####
response = client.associate_product_with_portfolio(
    AcceptLanguage='en',
    ProductId=s3_encrypted_bucket_product_id,
    PortfolioId=portfolio_id,
)
print ("PRODUCT/PORTFOLIO ASSOCIATED: Amazon S3 Encrypted Bucket")
print ("--id=" + s3_encrypted_bucket_product_id)
print ("")


#####
# Create Product: Amazon S3 Private Bucket with MFA Delete Restrictions
#####
token = "token"+str(int(random.random()*8765309))
response = client.create_product(
    AcceptLanguage='en',
    Name='Amazon S3 Private Bucket with MFA Delete Restrictions',
    Description='This product builds an Amazon AWS S3 bucket with multi-factor authentication restricted bucket delete option.',
    Owner=product_owner,
    Distributor=product_distributor,
    SupportDescription=support_description,
    SupportEmail=support_email,
    SupportUrl=support_url,
    ProductType=product_type,
    Tags=[
        {
            'Key': 'ProductType',
            'Value': 'Amazon S3 Private Bucket with MFA Delete Restrictions'
        }
    ],
    ProvisioningArtifactParameters={
        'Name': 'v1.0',
        'Description': 'baseline version',
        'Info': {
            "LoadTemplateFromURL" : "https://raw.githubusercontent.com/aws-samples/aws-service-catalog-reference-architectures/master/s3/sc-s3-mfa-ra.json"
        },
        'Type': 'CLOUD_FORMATION_TEMPLATE'
    },
    IdempotencyToken=token
)
s3_mfa_bucket_product_id = response['ProductViewDetail']['ProductViewSummary']['ProductId']
print ("PRODUCT CREATED: Amazon S3 Private Bucket with MFA Delete Restrictions")


#####
# Associate Amazon S3 Private Bucket with MFA Delete Restrictions

response = client.associate_product_with_portfolio(
    AcceptLanguage='en',
    ProductId=s3_mfa_bucket_product_id,
    PortfolioId=portfolio_id,
)
print ("PRODUCT/PORTFOLIO ASSOCIATED: Amazon S3 Private Bucket with MFA Delete Restrictions")
print ("--id=" + s3_mfa_bucket_product_id)
print ("")


#####
# Create Product: Amazon S3 Private Bucket with Transition Ruleset
#####
token = "token"+str(int(random.random()*8765309))
response = client.create_product(
    AcceptLanguage='en',
    Name='Amazon S3 Private Bucket with Transition Ruleset',
    Description='This product builds an Amazon AWS S3 bucket with a transition ruleset to S3-IA and Glacier.',
    Owner=product_owner,
    Distributor=product_distributor,
    SupportDescription=support_description,
    SupportEmail=support_email,
    SupportUrl=support_url,
    ProductType=product_type,
    Tags=[
        {
            'Key': 'ProductType',
            'Value': 'Amazon S3 Private Bucket with Transition Ruleset'
        }
    ],
    ProvisioningArtifactParameters={
        'Name': 'v1.0',
        'Description': 'baseline version',
        'Info': {
            "LoadTemplateFromURL" : "https://raw.githubusercontent.com/aws-samples/aws-service-catalog-reference-architectures/master/s3/sc-s3-transition-ra.json"
        },
        'Type': 'CLOUD_FORMATION_TEMPLATE'
    },
    IdempotencyToken=token
)
s3_mfa_transition_product_id = response['ProductViewDetail']['ProductViewSummary']['ProductId']
print ("PRODUCT CREATED: Amazon S3 Private Bucket with Transition Ruleset")


#####
# Associate Amazon S3 Private Bucket with Transition Ruleset

response = client.associate_product_with_portfolio(
    AcceptLanguage='en',
    ProductId=s3_mfa_transition_product_id,
    PortfolioId=portfolio_id,
)
print ("PRODUCT/PORTFOLIO ASSOCIATED: Amazon S3 Private Bucket with Transition Ruleset")
print ("--id=" + s3_mfa_transition_product_id)
print ("")

#####
# End Process
#####
print ("FINISHED -- Setup of Service Catalog S3 Reference Architecture.")
print ("")
