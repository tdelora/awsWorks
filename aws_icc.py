import sys,boto3
from botocore.exceptions import ClientError

def aws_instance_state(instanceIdReq):
        ec2 = boto3.client('ec2')

        try:
                response = ec2.describe_instances()
        except ClientError as e:
	        # Somthing went wrong with the describe instances query
		# print(e.response)
                print("aws_icc.aws_instance_state: Unexpected error: %s" % e)
        else:
                instanceList = response.get('Instances')
                if instanceList:
                        # Somthing is running
                        for instanceDictionary in instanceList:
                                instanceId = instanceDictionary.get("InstanceId")
                                if instanceId != None:
                                        if instanceId == instanceIdReq:
                                                print("Instance: %s" % instanceDictionary)
                                                break
                                                



def aws_create_instance(iid,it,kn):
	ec2_resource = boto3.resource('ec2')

	instance = ec2_resource.create_instances(
        ImageId=iid,
        MinCount=1,
        MaxCount=1,
        InstanceType=it,
        KeyName=kn)

	return instance
