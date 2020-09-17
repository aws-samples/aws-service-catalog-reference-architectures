## Using AWS Service Catalog to deploy SAP HANA components



Many Organizations have use cases to quickly deploy components used by SAP HANA in a simple, easy to use repeatable manner. SAP HANA is used by thousands of companies to run their business, having a simple repeatable process to deploy SAP infrastructure is critical for these businesses. 

I will show you how to use how AWS Launch Wizard and AWS Service Catalog together to simplify the deployment of SAP components on the AWS Cloud.
This solution uses the following AWS services. Most of the resources are set up for you with an AWS CloudFormation stack:

- AWS Service Catalog
- AWS Lambda
- AWS Launch Wizard
- AWS CloudFormation

### Solution overview


Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")



The following diagram maps out the solution architecture. 
![alt text][https://s3.amazonaws.com/aws-service-catalog-reference-architectures/sap/sc_scp.png]


To get started now, just sign in to your AWS account and click the button to create a Service Catalog Portfolio with sample EC2 products in your AWS account:
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation#/stacks/new?stackName=SC-RA-EC2Portfolio&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/ec2/sc-portfolio-ec2demo.json)  
