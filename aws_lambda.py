import boto3
from botocore.exceptions import ClientError
import os
import sys

def trigger_event(function,payload):

    client = boto3.client('lambda')
    try:
        response = client.invoke(
        FunctionName=function,
        InvocationType='Event',
        Payload=payload)
    except ClientError as e:
                # Somthing went wrong with the invokation
                print("aws_lamda.trigger_event: %s" % e)
    else:
        print(response)

    # return(response)