# snapshotalyzer-30001
Demo project to manage EC2 instance snapshots

##About

This project is a demo, and uses boto3 to manage AMS EC2 instance snapshots

##Config file used
aws configure --profile Chitti

##RUnnign the codepkg

`pipenv run python cnt_ec2_cde\shotty.py <command> <--project=PROJECT>`

*command* is list instances, volumes or snapshots; start or stop instances
*PROJECT* is the project tag value of the instnances and optional

help function is available for all Commands
