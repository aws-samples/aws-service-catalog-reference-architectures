
## Using AWS Control Tower and AWS Service Catalog to automate Control Tower lifecycle events ##
 


Many enterprise customers who use AWS Control Tower to create accounts want a way to extend the account creation process. They want this process to cover common business use cases including the creation of networks, security profiles, governance, and compliance. A manual process manually is cumbersome and makes it difficult for the organization to respond to the needs of its business. It might also be expensive if the organization pays another party to manage this process.

In this blog post, we will show you how to automate steps after an account is created. Each step can be unique to an organizational unit (OU) by placing the name of a template or infrastructure as code (IaC) in a tag on the OU. An OU can have multiple tags, one per lifecycle event. After each lifecycle event, the template in the tag is executed to support the customer's use case.
This solution we describe in the post uses the following AWS services. Most of the resources are set up for you with an AWS CloudFormation stack:
