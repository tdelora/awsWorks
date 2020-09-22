import boto3
from botocore.exceptions import ClientError
import os
import sys

def aws_kp_check(kp_name):
	returnValue = "create"
	ec2_client = boto3.client('ec2')
	response = ec2_client.describe_key_pairs()

	"""
	print(response)
	print(type(response))
	"""
	
	# response is a dictionary, time to dig in.
	try:
		kpdl = response['KeyPairs']
		if kpdl:
			# kpdl is a (non empty) list full of dictionaries with exiting key pair information
			for kpd in kpdl:
				# There may be multiple keypairs so we will have to iterate thru the list
				value = kpd.get("KeyName")
				if (value != None):
					# print("KeyName: " + value)
					if value == kp_name:
						returnValue = kp_name
						break
	except KeyError:
		# This should not happen unless they changed the return JSON
		print("aws_kpc.aws_kp_check: List KeyPairs not found")
		returnValue = "quit"

	return returnValue

def aws_kp_create(kp_name):
	ec2_client = boto3.client('ec2')
	os_detect = sys.platform
	returnValue = 0
	df = os.getenv("HOME")
	
	if os_detect == 'darwin':
		# MacOS
		df = df + "/Downloads/" + kp_name + ".pem"
	else:
		# Just put in home directory
		df = df + "/" + kp_name + ".pem"
	print("Creating keypair " + df)
	# print(df)

	try:
		response = ec2_client.create_key_pair(KeyName=kp_name)
		km = response['KeyMaterial']
		# print(km)
		pem_file = open(df,"w")
		n = pem_file.write(km)
		pem_file.close()
		returnValue = n

	except ClientError as e:
		# Somthing went wrong with keypair creation
		# print(e.response)
		if e.response['Error']['Code'] == 'InvalidKeyPair.Duplicate':
			# This will print if the keypair is a duplicate
			print("aws_kpc.aws_kp_create: " + e.response['Error']['Message'])
		else:
			# This will print any other boto3 error
			print("aws_kpc.aws_kp_create: Unexpected error: %s" % e)
	except KeyError:
		# This should not happen unless the response JSON has changed
		print("aws_kpc.aws_kp_create: Dictionary key KeyMaterial not found")
	except Exception as e:
		# This will handle any errors due to file open and write
		print("aws_kpc.aws_kp_create: %s" % e)

	return returnValue
