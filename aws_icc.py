import sys,boto3
from botocore.exceptions import ClientError

def get_instances_and_state():
        ec2 = boto3.client('ec2')
        isdList = []

        try:
                response = ec2.describe_instances()
        except ClientError as e:
	        # Somthing went wrong with the describe instances query
		# print(e.response)
                print("aws_icc.get_instances_and_state: Unexpected error: %s" % e)
        else:
                reservationsList = response.get('Reservations')
                for listData in reservationsList:
                        instanceInfo = listData.get("Instances")
                        for info in instanceInfo:
                                instanceId = info['InstanceId']
                                state = info['State']
                                stateCode = state.get('Code')
                                stateString = state.get('Name')
                                # print(instanceId,stateCode.stateString)
                                isDict = {'InstanceId':instanceId,'Code':stateCode,'Name':stateString}
                                isdList.append(isDict)
        return isdList

def aws_instance_state(instanceIdReq):
        stateCode = -1
        stateString = "notFound"

        isdList = get_instances_and_state()

        for isd in isdList:
                instanceId = isd.get('InstanceId')
                if instanceId == None:
                        print("aws_icc.aws_instance_state: InstanceId not found!")
                else:
                        if instanceId == instanceIdReq:
                                stateCode = isd.get('Code')
                                stateString = isd.get('Name')
                                break
                
        return(stateCode,stateString)
                                                
def aws_create_instance(iid,it,minC,maxC,kn):
	ec2_resource = boto3.resource('ec2')

	instance = ec2_resource.create_instances(
        ImageId=iid,
        MinCount=minC,
        MaxCount=maxC,
        InstanceType=it,
        KeyName=kn)

	return instance

def aws_get_instances_with_state(reqState):
        stateCode = -1
        inList = []
        # print(reqState)

        isdList = get_instances_and_state()

        for isd in isdList:
                stateCode = isd.get('Code')
                if stateCode == reqState:
                        instanceId = isd.get('InstanceId')
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