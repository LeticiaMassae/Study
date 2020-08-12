# https://www.youtube.com/watch?v=paxTBtfYtMU

import boto3
from pprint import pprint

ec2 = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

print("-= ec2.instances.all() =-")
for each_in in ec2.instances.all():
    pprint(dir(each_in))
    break
