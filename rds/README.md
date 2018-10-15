Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
  
  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at
  
      http://www.apache.org/licenses/LICENSE-2.0
  
  or in the "license" file accompanying this file. This file is distributed 
  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
  express or implied. See the License for the specific language governing 
  permissions and limitations under the License.


# AWS Service Catalog RDS Reference blueprint

This reference blueprint demonstrates how an organization can leverage Serivce Catalog to provide Amazon Relation Database Service (RDS) databases testing and integration..  

## Getting Started

When implemented this reference blueprint creates a AWS Service Catalog Portfolio called "AWS Service Catalog RDS Reference Architecture" with four associated products.  The AWS Service Catalog Products reference RDS database cloudformation templates for PostgreSQL, MySQL, MariaDB, Microsoft SQL which can be lauched by end users through AWS Service Catalog as either single instance databases or multi-availability zone databases.

### Single Instance Architecture

![sc-rds-ra-architecture-single-instance.png](sc-rds-ra-architecture-single-instance.png)


### Multi-Availability Zone Architecture

![sc-rds-ra-architecture-multi-az.png](sc-rds-ra-architecture-multi-az.png)

### For detailed instructions on how to set up this AWS Service catalog product and portfolio, see [Walkthrough Guide](sc-rds-ra-walkthrough.pdf)



Note - Before you distribute this CloudFormation template, review the template and ensure that it is doing what you want it to do. Check IAM permissions, Deletion policies, and other aspects of the template to ensure that they are as per your expectations.


## License

* This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details

 
