# Cloud Watch monitor with Lambda function.

## About Function
In the repository there is lambda code (lambda.py) that create AWS cloud watch alarms when a new instance is launched . As the alram will be at ok stage or at alarm stage a mail is send to a particular mail id . This mail id set by environment variable e_mailid which take SNS as it's value.

###### Packages required:
  - The code requires  python3 and boto3
  
###### Installation 
 * create a lamdba function with Python 3.7 compiler 
    * role having access to AmazonEC2,CloudWatch,AmazonSNS
    * rule  Service Name 
      - Under cloud watch need to create rule . Select Event Patterns 
      - Here, Service Name is set to Auto Scaling 
      - Event type is set to Instance Launch and Terminate 
      - Specific Instance event(s) is set to EC2 Instance Launch Successful	    
      - Select Any group name 
      - Under Lambda Funtion is  given the  lambda  function name and give name  to the rule 
	
* create Environment variables
  - Mem_Thr_byte : 500000000 <vlaue  in bytes>
  - SNS_Topic : sns  
  - TagName : Name
  - TagValue: value (alram will trigger for those instances which have  this value)
  
	
* Paste the code save and test by lauching a new instance 

 
