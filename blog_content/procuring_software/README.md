Procuring software on AWS Marketplace
for customers in regulated spaces
Customers operating in highly-regulated spaces often tell us about the compliance challenges 
that they face when procuring commercial software in the cloud. This is especially true for 
federal customers subject to the GSA Schedule   , or state and local customers operating under 
NASPO Value Point. Procurements in this space often require negotiated purchasing agreements 
and custom terms between the vendor and buyer. For these customers, it’s paramount that 
purchasing agreements are made by a central governing group to minimize the risk of 
noncompliant agreements. To solve this challenge for customers, we’ve created a centralized 
software procurement and distribution solution using AWS Marketplace Private Offers, License 
Manager, and AWS Identity and Access Management (IAM)    that gives customers the flexibility 
to procure using custom purchasing agreements while maintaining complete governance. 
In this post, we present a method for centralizing the procurement and distribution of AWS 
Marketplace software that is intended to get customers into highly-regulated environments up 
and running with AWS Marketplace. We utilize IAM roles to govern who has access to the AWS
Marketplace subscribe and license distribution actions. Then, we set up AWS License Manager    
for the distribution of AWS Marketplace software licenses from a central account. After setting 
up the solution, we demonstrate its use through the experiences of the three personas, defined as 
follows:
Procurement Manager – This persona is responsible for negotiating 
terms and conditions with the AWS Marketplace software vendor. This 
persona has the permission to accept AWS Marketplace offers.
Software Manager – This persona is responsible for distributing 
access to the procured software using license grants in License 
Manager. This persona has permission to distribute and activate 
licenses, but it can’t accept AWS Marketplace offers.
End User – This persona is a consumer of the procured software. This 
persona can’t accept AWS Marketplace offers. This persona can only 
accept software licenses that have been sent to them by the Software 
Manager. 
