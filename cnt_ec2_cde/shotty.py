import boto3
import click

session = boto3.Session(profile_name = 'Chitti')
ec3 = session.resource('ec2')

@click.command()
@click.option('--project', default=None,
    help="only instances for project (tag Project:<name>)")
def list_instances(project):
    "List EC2 instances"
    instances=[]
    if project:
        filters = [{'Name':'tag:Project','Values':[project]}]
        instances = ec3.instances.filter(Filters=filters)
    else:
        instances = ec3.instances
    for i in ec3.instances.all():
        tags = {t['Key']:t['Value']} for t in i.tags or []}
        print(', '.join((
        i.id,
        i.instance_type,
        i.placement['AvailabilityZone'],
        i.state['Name'],
        i.public_dns_name
        tags.get('Project','<No Project>')
        ))
        )

if __name__=='__main__':
    list_instances()
