from setuptools import setup

setup(
    name='snapshotalyzer-30001',
    version='0.1',
    author="Xenon",
    author_email='charansritej@outlook.com',
    description="Snapshotalyzer is a utility to manage aws ec2 volume snapshots",
    license="GPLv3+",
    packages=['cnt_ec2_cde'],
    url="https://github.com/XenonDust/snapshotalyzer-30001",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        xenon=cnt_ec2_cde.shotty:cli
    ''',

)
