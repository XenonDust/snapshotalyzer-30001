import boto3
import sys

session = boto3.Session(profile_name = 'Chitti')
ec3 = session.resource('ec2')

def list_instances():
    for i in ec3.instances.all():
        print(i)

if __name__=='__main__':
    print(sys.argv)
    list_instances()
