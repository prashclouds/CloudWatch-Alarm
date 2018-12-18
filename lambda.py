import boto3
import json
import logging
import os
# Create AWS clients
#ec2session = boto3.client('ec2')

ec2session = boto3.resource('ec2')
cw = boto3.client('cloudwatch')

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

# Retrieves instance id from CloudWatch event
def get_instance_id(event):
    try:
        return event['detail']['EC2InstanceId']
    except KeyError as err:
        LOGGER.error(err)
        return False

def get_metadata(event):
    try:
        return event
    except KeyError as err:
        LOGGER.error(err)
        return False
        
def get_inststat(event):
    try:
        return event['detail-type']
    except KeyError as err:
        LOGGER.error(err)
        return False


def lambda_handler(event, context):

    session = boto3.session.Session()
    #ec2session = session.client('ec2')
    #y = testenv
    instanceid = get_instance_id(event)
    metadata = get_metadata(event)
    instancestat = get_inststat(event)
    LOGGER.info("instance-id: %s" % instanceid)
    LOGGER.info("EVENT SEND BY : %s" % event)
    LOGGER.info("instance status   : %s" % instancestat)
    mysns = os.environ['e_mailid']
    mytag = os.environ['e_tag']
    
    if instancestat == 'EC2 Instance Launch Successful':
          
        LOGGER.info("Environment Varible test : %s" % mysns)
        ec2instance = ec2session.Instance(instanceid)
        instancetag= ''
        for tags in ec2instance.tags:
            if tags["Key"] == mytag:
                instancetag = tags["Value"]
                print(instancetag)
                LOGGER.info("TAG : %s" % instancetag)
        
        
        # Create alarm
        cw.put_metric_alarm(
        AlarmName='Web_Server_CPU_Utilization is  high on %s' % instanceid,
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=1,
        MetricName='CPUUtilization',
    #   MetricName='CP',
        Namespace='AWS/EC2',
        Period=300,
        Statistic='Average',
        Threshold=70.0,
        ActionsEnabled=True,
        AlarmActions=[

            mysns
      
        ],
        OKActions=[
            mysns
        ],
        AlarmDescription='Alarm when server CPU exceeds 70%',
        Dimensions=[
            {
            'Name': 'InstanceId',
            'Value': instanceid
            },
        ],
        #Unit='Seconds'
    )

        cw.put_metric_alarm(
        AlarmName='Instance Stauts Check %s' % instanceid,
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=1,
        MetricName='StatusCheckFailed_Instance',
    #   MetricName='CP',
        Namespace='AWS/EC2',
        Period=300,
        Statistic='Average',
        Threshold=1.0,
        ActionsEnabled=True,
        AlarmActions=[
            mysns
       
        ],
        OKActions=[
            mysns
        ],
        AlarmDescription='Status Check Failed',
        Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': instanceid
            },
        ],
    )  
