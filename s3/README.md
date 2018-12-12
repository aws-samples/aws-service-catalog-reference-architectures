# AWS Service Catalog S3 Reference blueprint

This reference blueprint demonstrates how an organization can leverage Serivce Catalog to provide Amazon Simple Storage Service (S3)) buckets with various configurations for testing and integration.

## Getting Started

When implemented this reference blueprint creates an AWS Service Catalog Portfolio called "Service Catalog S3 Reference Architecture" with five associated products.  The AWS Service Catalog Product references cloudformation templates for the Amazon S3 buckets which can be lauched by end users through Service Catalog.  The AWS Service Catalog S3 products create S3 buckets with varying configurations: 1) Read-Only bucket with access from anywhere, 2) Private bucket with access restricted to a source CIDR block, 3) Private bucket with access requiring multi-factor authentication, 4) Private bucket with contents encrypted with S3 server side encryption, and 5) Private bucket with a transition ruleset to migrate innactive objects to S3-IA and Glacier. 

### AWS S3 public Access read-only bucket

![sc-s3-public-ra-architecture.png](sc-s3-public-ra-architecture.png)

### AWS S3 private bucket with restricted access from source CIDR block

![sc-s3-cidr-ra-architecture.png](sc-s3-cidr-ra-architecture.png)

### AWS S3 Private SSE-S3 Encrypted Bucket

![sc-s3-encyprted-ra-architecture.png](sc-s3-encrypted-ra-architecture.png)

### AWS S3 Private MFA Restricted Access Bucket

![sc-s3-mfa-ra-architecture.png](sc-s3-mfa-ra-architecture.png)

### AWS S3 Private Bucket with transition policy for S3-IA and Glacier

![sc-s3-transition-ra-architecture.png](sc-s3-transition-ra-architecture.png)


### For detailed instructions on how to set up this AWS Service catalog product and portfolio, see [Walkthrough Guide](sc-s3-ra-walkthrough.pdf)


Note - Before you distribute this CloudFormation template, review the template and ensure that it is doing what you want it to do. Check IAM permissions, Deletion policies, and other aspects of the template to ensure that they are as per your expectations.


## License

* This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details
Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

 
