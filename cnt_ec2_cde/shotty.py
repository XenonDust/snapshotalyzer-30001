import boto3

if __name__=='__main__':
    session = boto3.Session(profile_name = 'Chitti')
    ec3 = session.resource('ec2')

    for i in ec3.instances.all():
        print(i)
