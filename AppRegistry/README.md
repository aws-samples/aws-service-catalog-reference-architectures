# AWS Service Catalog AppRegistry reference architecture

This reference architecture creates an AWS Service Catalog AppRegistry Application and Attribute group. 
For an example of how to automatically associatge AWS Service Catalog products with AppRegistry see this [sample EC2 template with AppRegistry](https://github.com/aws-samples/aws-service-catalog-reference-architectures/blob/master/ec2/sc-ec2-linux-nginx-nokey-appreg.json).

### Try this in your account:
1. Launch the AppRegistry stack below
2. Add the [sample EC2 template with AppRegistry](https://github.com/aws-samples/aws-service-catalog-reference-architectures/blob/master/ec2/sc-ec2-linux-nginx-nokey-appreg.json) as a version or product in AWS Service Catalog.
3. Provision the EC2 product from [AWS Service Catalog](https://console.aws.amazon.com/servicecatalog/#products).
4. Review the associated resources in AppRegistry found in the [AWS Service Catalog console](https://console.aws.amazon.com/servicecatalog/#applications/).


[Admin Guide](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/appregistry.html)


See how to create and query an AWS Service Catalog AppRegistry Application with CLI: 
[Increase application visibility and governance using AWS Service Catalog AppRegistry](https://aws.amazon.com/blogs/mt/increase-application-visibility-governance-using-aws-service-catalog-appregistry/)
 

### Install  
Launch the AppRegistry stack:  
[![CreateStack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=SC-RA-AppRegistryExample&templateURL=https://s3.amazonaws.com/aws-service-catalog-reference-architectures/AppRegistry/sc-appreg-example.json)  


