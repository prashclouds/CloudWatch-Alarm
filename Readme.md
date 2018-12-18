# Project Title
## Cloud Watch monitor with Lambda function.

## About Function
In the repository there is lambda code (lambda.py) that create AWS cloud watch alarms when a new instance is launched . As the alram will be at ok stage or at alarm stage a mail is send to a particular mail id . This mail id set by environment variable e_mailid which take SNS as it's value.

###### Packages required:
  - The code requires additional python3 packages boto3
  
###### Installation 
 * create a lamdba function with Python 3.7 compiler 
    * role having access to AmazonEC2,CloudWatch,AmazonSNS
    * rule  Service Name : Auto Scaling, Event Type : Instance Launch and Terminate,Slecet Specific  Instance event(s)
	Ec2 Instance Launch Successful
* create Environment variables 
    * e_mailid : SNS 
* Paste the code save and test by lauching a new instance 

 
