import boto3
import click

session = boto3.Session(profile_name = 'Chitti')
ec3 = session.resource('ec2')

def filter_instances(project):
    instances = []

    if project:
        filters = [{'Name':'tag:Project','Values':[project]}]
        instances = ec3.instances.filter(Filters=filters)
    else:
        instances = ec3.instances.all()
    return instances

@click.group()
def cli():
    """Shotty manages snapshots"""

@cli.group('volumes')
def volumes():
    """Commands for volumnes"""

@volumes.command('list')
@click.option('--project', default=None,
    help="only volumes for project (tag Project:<name>)")
def list_volumes(project):
    "List EC2 volumes"

    instances = filter_instances(project)

    for i in instances:
        for v in i.volumes.all():
            print(", ".join((
            v.id,
            i.id,
            v.state,
            str(v.size) + "GiB",
            v.encrypted and "Encrypted" or "Not Encrypted"
            )))
    return

@cli.group('snapshots')
def snapshots():
    """Commands for snapshots"""

@snapshots.command('list')
@click.option('--project', default=None,
    help="only snapshots for project (tag Project:<name>)")
def list_snapshots(project):
    "List EC2 Volume Snapshots"

    instances = filter_instances(project)
    for i in instances:
        for v in i.volumes.all():
            for s in v.snapshots.all():
                print(", ".join((
                s.id,
                v.id,
                i.id,
                s.state,
                s.progress,
                s.start_time.strftime("%c")
                )))
    return


@cli.group('instances')
def instances():
    """Commands for instances"""

@instances.command('list')
@click.option('--project', default=None,
    help="only instances for project (tag Project:<name>)")
def list_instances(project):
    "List EC2 instances"

    instances = filter_instances(project)

    for i in instances:
        tags = {t['Key']:t['Value'] for t in i.tags or []}
        print(', '.join((
        i.id,
        i.instance_type,
        i.placement['AvailabilityZone'],
        i.state['Name'],
        i.public_dns_name,
        tags.get('Project','<No Project>')
        ))
        )
    return

@instances.command('stop')
@click.option('--project', default=None, help=
'Only instances for project')
def stop_instances(project):
    "Stop EC2 instances"

    instances = filter_instances(project)

    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()
    return

@instances.command('start')
@click.option('--project', default=None, help=
'Only instances for project')
def stop_instances(project):
    "Stop EC2 instances"

    instances = filter_instances(project)

    for i in instances:
        print("Starting {0}...".format(i.id))
        i.start()
    return


@instances.command('snapshot', help="Create snapshots of all volumes")
@click.option('--project', default=None, help="Only instances for project(tab Project:<name>)")

def create_snapshot(project):
    "Create snapshots for EC2 instances"

    instances = filter_instances(project)

    for i in instances:
        i.stop()
        for v in i.volumes.all():
            print("Creating snapshot of {0}".format(v.id))
            v.create_snapshot(Description= "Created by Snapshotalyzer")
    return

if __name__=='__main__':
    cli()
