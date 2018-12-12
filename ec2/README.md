Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
  
  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at
  
      http://www.apache.org/licenses/LICENSE-2.0
  
  or in the "license" file accompanying this file. This file is distributed 
  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
  express or implied. See the License for the specific language governing 
  permissions and limitations under the License.

# AWS Service Catalog EC2 Reference blueprint

This reference blueprint demonstrates how an organization can leverage Serivce Catalog to provide Amazon Elastic Compute (EC2) instances and Simple Systems Manager (SSM) instance patching for testing and integration.

## Getting Started

When implemented this reference blueprint creates an AWS Service Catalog Portfolio called "Service Catalog EC2 Reference Architecture" with two associated products.  The AWS Service Catalog Product references cloudformation templates for the Amazon EC2 Linux and Windows instances which can be lauched by end users through AWS Service Catalog.  The AWS Service Catalog EC2 product creates either an Aamzon Linux or Microsoft Windows EC2 instance in the VPC and Subnets selected by the end user.  A Amazon Simple Systems Manager patch baseline, maintenance window and task are created to allow for automated patching of the Aamzon Linux and Microsoft Windows operating systems.

### Create Stack

In the AWS CloudFormation console choose "Create Stack" and supply the Portfolio url:  
[sc-portfolio-ec2.json](sc-portfolio-ec2.json)

Or, just click this button:
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SCRAEC2Portfolio&templateURL=https://raw.githubusercontent.com/chapmancl/aws-service-catalog-reference-architectures/master/ec2/sc-portfolio-ec2.json)


### EC2 Architecture with Amazon Linux and Microsoft Windows instances

![sc-ec2-ra-architecture.png](sc-ec2-ra-architecture.png)

### For instructions detailed instructions on how to set up this AWS Service catalog product and portfolio, see [Walkthrough Guide](sc-ec2-ra-walktrough.pdf)

Note - Before you distribute this CloudFormation template, review the template and ensure that it is doing what you want it to do. Check IAM permissions, Deletion policies, and other aspects of the template to ensure that they are as per your expectations.


## License

* This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details

 
