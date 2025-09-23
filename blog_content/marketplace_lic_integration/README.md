### AWS Marketplace - AWS License Manager integration

Execute the cloudformation template mp-lm-one-time-configuration.yaml from management account to setup Integration between AWS license manager and AWS Marketplace

 WARNING: This CloudFormation template creates 2 AWS lambdas OrganizationsSettingsUpdateLambda and LicenseManagerSettingsUpdateLambda to update settings. Please remember to delete these lambdas once Cloudformation execution completes.
