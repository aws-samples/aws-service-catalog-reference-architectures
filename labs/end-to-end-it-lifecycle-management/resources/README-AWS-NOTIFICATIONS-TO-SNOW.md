[⌂ Home](/labs/end-to-end-it-lifecycle-management/README.md)
[< Back](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-PROVISIONING.md)

# Set up automatic incident creation in ServiceNow 

In this task, you will configure your AWS account to send a notification and create an incident in the ServiceNow instance. As a part of the _Lab Setup_, we have pre-provisioned a custom AWS Config rule in your AWS account that flags any EC2 instance that does not have `t2.micro` as an instance type, as a non-compliant resource. 

To use the AWS config rule that we created for you and set up notifications to ServiceNow, follow the steps below:

### Set up AWS Config 
1. In your AWS console, You need to go back to switch your role back to awsstudent user (you can find the URL to launch in cloudformation output under key `SwitchRoleAwsStudent`).
2. Next, in the services tab, navigate to `AWS Config`.
3. Choose `Get Started`
4. On the settings screen, under resource types to record, uncheck `All resources`,
5. Under `Specific types`, specify `EC2:Instance` as Resource types to record.
6. Under `Amazon S3 bucket`, choose choose the bucket from your account and specify bucket provided to you in the `Outputs` section of the Cloudformation(the bucket will have configbucket in its name)
7. Under `AWS Config role`, choose `Use an existing AWS Config service-linked role` and then choose `Next`.
8. On AWS Config Rules screen, choose `Skip`.
9. On Review screen, choose `Confirm`.
![snow-incident-1](/labs/end-to-end-it-lifecycle-management/resources/snow-incident-1.png)

### Configure AWS Config Rules
1. Choose `Rules` from the left panel, this will open the AWS Config rules that have been configured in your AWS account.
2. Next, choose the `ConfigRuleForCheckIfInstanceIsNotOfTypeT2MicroVerification` rule to view the rule details.
3. Note the `trigger type` - the values are configuration changes and periodic. The rule has been configured to trigger re-evaluation every time an EC2 instance starts/stops/terminates.
4. Note the `Resources evaluated` section. Later, after you launch an EC2 instance in your environment, you will find that non-compliant as well as, compliant resources appear here.

Next, you need to view the `CloudWatch Events rule` which publishes compliance change notifications for the config rule `ConfigRuleForCheckIfInstanceIsNotOfTypeT2MicroVerification`.

### Set up CloudWatch Events rule
1. Open `CloudWatch` by launching following link - `https://console.aws.amazon.com/cloudwatch/`
2. Ensure you are in correct region.
3. Choose `Rules` in left panel, choose the name `T2MicroConfigRuleComplianceChangeNotification` to open it. You will see that the CloudWatch events rule publishes a notification everytime `ComplianceChangeNotification` message is published by the Config rule you viewed earlier, on `T2MicroConfigRuleTopic` SNS topic.
![snow-incident-2](/labs/end-to-end-it-lifecycle-management/resources/snow-incident-2.png)

### Set up the AWS SNS subscription to the CloudWatch Event rule in the previous step
1. Open SNS service by launching `https://console.aws.amazon.com/sns/` in a browser tab, ensure that you are in the correct region.
2. Choose `Topics` from left panel and then click on ARN of the `T2MicroConfigRuleTopic` topic that is pre-configured for you to view the topic details.
3. Under `Subscriptions`, choose `Create Subscription` to create a subscription for ServiceNow.
4. Choose `Https` as the protocol
5. Specify your ServiceNow instance URL as the endpoint:
    1. `https://admin:<ServiceNow admin password>@<your developer instance>.service-now.com/api/x_snc_aws_sns/aws_sns`
    2. Note: If `https://rel-oct12shm-005.lab.service-now.com/` is your ServiceNow URL, then `rel-oct12shm-005.lab` is the value of your developer instance)
    3. Here is an example of a value: `https://admin:mypassword@rel-oct12shm-005.lab.service-now.com/api/x_snc_aws_sns/aws_sns`
![snow-incident-3](/labs/end-to-end-it-lifecycle-management/resources/snow-incident-3.png)
6. Before you click on `Create subscription`, specify password and developer instance name in the endpoint.
7. Next, Choose `Create Subscription`.

### AWS SNS Subscription confirmation in ServiceNow
Now you will log in to your ServiceNow instance and accept the pending subscription. Before `AWS SNS` is allowed to send messages to ServiceNow, you must confirm the subscription on ServiceNow. 
At this point, AWS has already sent a handshake request, and it’s awaiting confirmation inside your ServiceNow instance.
Next, choose `Subscriptions` under `AWS SNS` by using the filter in the left panel of your ServiceNow screen, and notice that a new record has been created by AWS.
![snow-incident-4](/labs/end-to-end-it-lifecycle-management/resources/snow-incident-4.png)
Open the subscription by choosing the name displayed(E.g. in above screenshot, ServiceNow), and then choose `Confirm Subscription`.

Stay on this page for the next step.
![snow-incident-5](/labs/end-to-end-it-lifecycle-management/resources/snow-incident-5.png)

### Set up script in ServiceNow to handle notification

Now let’s do something meaningful whenever `AWS SNS` sends a notification to ServiceNow. ServiceNow provides a script `Handler` that is invoked when SNS sends an alarm message. To configure a handler to create an incident, follow the instructions below:
- At the bottom of the Subscription form,find the Handlers section.
![snow-incident-6](/labs/end-to-end-it-lifecycle-management/resources/snow-incident-6.png)
- Choose `New` and type a name for the handler, such as `Create SNS Non-micro launch Incident`. 
- Replace the entire function with below text:
```sh
// SNS Message payload is available as the 'message' object
(function(message){
	// e.g. handle config item change
	if(message.detail.newEvaluationResult.complianceType =='NON_COMPLIANT'){
		var incident = new GlideRecord("incident");
		incident.initialize();
		incident.caller_id = gs.getUserID();
		incident.short_description = "SNS Alarm: "+message.detail.configRuleName;
		incident.description = "AWS Account ID: " + message.account + "\nRegion: " + message.detail.awsRegion + "\nCompliance status: " + message.detail.newEvaluationResult.complianceType; 
        incident.insert();
		}
}(message));
```
- Choose `Submit` to save the handler. Here is how your code will look.
![snow-incident-7](/labs/end-to-end-it-lifecycle-management/resources/snow-incident-7.png)


[Next: Trigger incident creation in ServiceNow from AWS >>](/labs/end-to-end-it-lifecycle-management/resources/README-SNOW-INCIDENT-CREATION.md)

