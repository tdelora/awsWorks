import sys,boto3

def aws_create_instance(iid,it,kn):
	ec2_resource = boto3.resource('ec2')

	instance = ec2_resource.create_instances(
        ImageId=iid,
        MinCount=1,
        MaxCount=1,
        InstanceType=it,
        KeyName=kn)

	return instance
