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
print ("STARTED -- Setup of Service Catalog RDS Reference Architecture.")
print ("")

#####
# Create Portfolio
#####
token = "token"+str(int(random.random()*8675309))
response = client.create_portfolio(
    AcceptLanguage='en',
    DisplayName='Service Catalog RDS Reference Architecture',
    Description='Service Catalog Portfolio that contains reference architecture products for Amazon Relational Database Service.',
    ProviderName=product_owner,
    Tags=[
        {
            'Key': 'Portfolio',
            'Value': 'Service Catalog RDS Reference Architecture'
        }
    ],
    IdempotencyToken=token
)
portfolio_id = response['PortfolioDetail']['Id']
portfolio_arn = response['PortfolioDetail']['ARN']
print ("PORTFOLIO CREATED: Service Catalog RDS Reference Architecture")
print ("--id=" + portfolio_id)
print ("--arn=" + portfolio_arn)
print ("")


#####
# Create Product: RDS PostgreSQL Database
#####
token = "token"+str(int(random.random()*8765309))
response = client.create_product(
    AcceptLanguage='en',
    Name='Amazon RDS PostgreSQL Database',
    Description='This product builds an Amazon AWS RDS PostgreSQL master database instance with options for a single instance or multi-az instances.',
    Owner=product_owner,
    Distributor=product_distributor,
    SupportDescription=support_description,
    SupportEmail=support_email,
    SupportUrl=support_url,
    ProductType=product_type,
    Tags=[
        {
            'Key': 'ProductType',
            'Value': 'AWS RDS PostgreSQL'
        }
    ],
    ProvisioningArtifactParameters={
        'Name': 'v1.0',
        'Description': 'baseline version',
        'Info': {
            "LoadTemplateFromURL" : "https://raw.githubusercontent.com/aws-samples/aws-service-catalog-reference-architectures/master/rds/sc-rds-postgresql-ra.json"
        },
        'Type': 'CLOUD_FORMATION_TEMPLATE'
    },
    IdempotencyToken=token
)
postgresql_product_id = response['ProductViewDetail']['ProductViewSummary']['ProductId']
print ("PRODUCT CREATED: Amazon RDS PostgreSQL Database")


#####
# Associate RDS PostgreSQL Product with Portfolio
#####
response = client.associate_product_with_portfolio(
    AcceptLanguage='en',
    ProductId=postgresql_product_id,
    PortfolioId=portfolio_id,
)
print ("PRODUCT/PORTFOLIO ASSOCIATED: Amazon RDS PostgreSQL Database")
print ("--id=" + postgresql_product_id)
print ("")


#####
# Create Product: RDS MySQL Database
#####
token = "token"+str(int(random.random()*8765309))
response = client.create_product(
    AcceptLanguage='en',
    Name='Amazon RDS MySQL Database',
    Description='This product builds an Amazon AWS RDS MySQL master database instance with options for a single instance or multi-az instances.',
    Owner=product_owner,
    Distributor=product_distributor,
    SupportDescription=support_description,
    SupportEmail=support_email,
    SupportUrl=support_url,
    ProductType=product_type,
    Tags=[
        {
            'Key': 'ProductType',
            'Value': 'AWS RDS MySQL'
        }
    ],
    ProvisioningArtifactParameters={
        'Name': 'v1.0',
        'Description': 'baseline version',
        'Info': {
            "LoadTemplateFromURL" : "https://raw.githubusercontent.com/aws-samples/aws-service-catalog-reference-architectures/master/rds/sc-rds-mysql-ra.json"
        },
        'Type': 'CLOUD_FORMATION_TEMPLATE'
    },
    IdempotencyToken=token
)
mysql_product_id = response['ProductViewDetail']['ProductViewSummary']['ProductId']
print ("PRODUCT CREATED: Amazon RDS MySQL Database")


#####
# Associate RDS MySQL Product with Portfolio
#####
response = client.associate_product_with_portfolio(
    AcceptLanguage='en',
    ProductId=mysql_product_id,
    PortfolioId=portfolio_id,
)
print ("PRODUCT/PORTFOLIO ASSOCIATED: Amazon RDS MySQL Database")
print ("--id=" + mysql_product_id)
print ("")


#####
# Create Product: RDS MariaDB Database
#####
token = "token"+str(int(random.random()*8765309))
response = client.create_product(
    AcceptLanguage='en',
    Name='Amazon RDS MariaDB Database',
    Description='This product builds an Amazon AWS RDS MariaDB master database instance with options for a single instance or multi-az instances.',
    Owner=product_owner,
    Distributor=product_distributor,
    SupportDescription=support_description,
    SupportEmail=support_email,
    SupportUrl=support_url,
    ProductType=product_type,
    Tags=[
        {
            'Key': 'ProductType',
            'Value': 'AWS RDS MariaDB'
        }
    ],
    ProvisioningArtifactParameters={
        'Name': 'v1.0',
        'Description': 'baseline version',
        'Info': {
            "LoadTemplateFromURL" : "https://raw.githubusercontent.com/aws-samples/aws-service-catalog-reference-architectures/master/rds/sc-rds-mariadb-ra.json"
        },
        'Type': 'CLOUD_FORMATION_TEMPLATE'
    },
    IdempotencyToken=token
)
mariadb_product_id = response['ProductViewDetail']['ProductViewSummary']['ProductId']
print ("PRODUCT CREATED: Amazon RDS MariaDB Database")


#####
# Associate RDS MariaDB Product with Portfolio
#####
response = client.associate_product_with_portfolio(
    AcceptLanguage='en',
    ProductId=mariadb_product_id,
    PortfolioId=portfolio_id,
)
print ("PRODUCT/PORTFOLIO ASSOCIATED: Amazon RDS MariaDB Database")
print ("--id=" + mariadb_product_id)
print ("")


#####
# Create Product: RDS Microsoft SQL Database
#####
token = "token"+str(int(random.random()*8765309))
response = client.create_product(
    AcceptLanguage='en',
    Name='Amazon RDS Microsoft SQL Database',
    Description='This product builds an Amazon AWS RDS Microsoft SQL master database instance with options for a single instance or multi-az instances.',
    Owner=product_owner,
    Distributor=product_distributor,
    SupportDescription=support_description,
    SupportEmail=support_email,
    SupportUrl=support_url,
    ProductType=product_type,
    Tags=[
        {
            'Key': 'ProductType',
            'Value': 'AWS RDS Microsoft SQL'
        }
    ],
    ProvisioningArtifactParameters={
        'Name': 'v1.0',
        'Description': 'baseline version',
        'Info': {
            "LoadTemplateFromURL" : "https://raw.githubusercontent.com/aws-samples/aws-service-catalog-reference-architectures/master/rds/sc-rds-mssql-ra.json"
        },
        'Type': 'CLOUD_FORMATION_TEMPLATE'
    },
    IdempotencyToken=token
)
mssql_product_id = response['ProductViewDetail']['ProductViewSummary']['ProductId']
print ("PRODUCT CREATED: Amazon RDS Microsoft SQL Database")


#####
# Associate RDS Microsoft SQL Product with Portfolio
#####
response = client.associate_product_with_portfolio(
    AcceptLanguage='en',
    ProductId=mssql_product_id,
    PortfolioId=portfolio_id,
)
print ("PRODUCT/PORTFOLIO ASSOCIATED: Amazon RDS Microsoft SQL Database")
print ("--id=" + mssql_product_id)
print ("")


#####
# End Process
#####
print ("FINISHED -- Setup of Service Catalog RDS Reference Architecture.")
print ("")
