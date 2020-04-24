## Service Catalog deploying AWS Config Conformance Packs 

A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed as a single entity in an account and a Region or across an organization in AWS Organizations. Conformance packs are created by authoring a YAML template that contains the list of AWS Config managed or custom rules and remediation actions. The following templates are intended to be samples for using AWS Config rules and remediation actions within a conformance pack. They do not guarantee thorough compliance check as is. You need to modify the template by adding more AWS Config rules to meet your AWS Organizations requirements and ensuring thorough compliance of your AWS resources.

**Note** These conformance packs are a part of the [Service Catalog Getting Started Library](https://console.aws.amazon.com/servicecatalog/home?#portfolios)

Conformance pack descriptions:

**sc_conformancepacks_prerequisites.yml**

  In order to utilize the Config Conformance Packs, step one is to execute this prerquisite template which will create an S3 bucket for all of the reporting associated to the conformance pack, as well as a service role that config conformance pack uses. Note- The Config Conformance Packs are intended to be samples for using AWS Config rules and remediation actions within a conformance pack. They do not guarantee thorough compliance check as is. You may need to modify the template by adding more AWS Config rules to meet your AWS Organizations requirements and ensuring thorough compliance of your AWS resources.
