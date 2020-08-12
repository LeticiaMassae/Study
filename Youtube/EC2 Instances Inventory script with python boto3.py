# https://www.youtube.com/watch?v=paxTBtfYtMU

import boto3
from pprint import pprint

ec2 = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

S_No=1
print("-= ec2.instances.all() =-")
for each_in in ec2.instances.all():
    IN_ID=each_in.instance_id
    IN_TYPE=each_in.instance_type
    IN_ARCH=each_in.architecture
    IN_VPC=each_in.public_ip_address
    print(S_No, IN_ID, IN_TYPE, IN_ARCH, IN_VPC)
    S_No=S_No+1