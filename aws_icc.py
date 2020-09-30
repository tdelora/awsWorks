import sys,boto3
from botocore.exceptions import ClientError

def aws_instance_state(instanceIdReq):
        ec2 = boto3.client('ec2')
        stateCode = -1
        stateString = "notFound"

        try:
                response = ec2.describe_instances()
        except ClientError as e:
	        # Somthing went wrong with the describe instances query
		# print(e.response)
                print("aws_icc.aws_instance_state: Unexpected error: %s" % e)
        else:
                reservationsList = response.get('Reservations')
                for listData in reservationsList:
                        instanceInfo = listData.get("Instances")
                        for info in instanceInfo:
                                instanceId = info['InstanceId']
                                if instanceId == instanceIdReq:
                                        state = info['State']
                                        stateCode = state.get('Code')
                                        stateString = state.get('Name')
                                        # print(instanceId,stateString)
        return(stateCode,stateString)
                                                
def aws_create_instance(iid,it,kn):
	ec2_resource = boto3.resource('ec2')

	instance = ec2_resource.create_instances(
        ImageId=iid,
        MinCount=1,
        MaxCount=1,
        InstanceType=it,
        KeyName=kn)

	return instance

def aws_get_instances_with_state(reqState):
        ec2 = boto3.client('ec2')
        stateCode = -1
        inList = []
        # print(reqState)

        try:
                response = ec2.describe_instances()
        except ClientError as e:
                # Somthing went wrong with the describe instances query
	        # print(e.response)
                print("aws_icc.aws_get_instances_with_state: Unexpected error: %s" % e)
        else:
                reservationsList = response.get('Reservations')
                for listData in reservationsList:
                        instanceInfo = listData.get("Instances")
                        for info in instanceInfo:
                                state = info['State']
                                stateCode = state.get('Code')
                                if stateCode == reqState:
                                        instanceId = info['InstanceId']
                                        # print(instanceId,stateCode)
                                        inList.append(instanceId)
        return inList

def aws_terminate_instance(instanceList):
        ec2_resource = boto3.resource('ec2')

        try:
                ec2_resource.instances.filter(InstanceIds=instanceList).terminate()
        except ClientError as e:
                # Somthing went wrong with the describe instances query
                # print(e.response)
                print("aws_icc.aws_terminate_instance: %s" % e)