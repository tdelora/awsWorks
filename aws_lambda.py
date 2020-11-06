import boto3
from botocore.exceptions import ClientError
import os
import sys

def trigger_event(function,payload):
    triggerSuccess = False
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
        # response is a dictionary
        metaData = response.get('ResponseMetadata')
        if metaData == None:
            # This should never happen unless they changed the response
            raise KeyError("aws_lambda.trigger_event: ResponseMetadata not found!")
        else:
            # metaData contains key pair HTTPStatusCode, we are checking for code 202
            # which means the event was accepted but not acted on yet.
            HTTPStatusCode = metaData.get('HTTPStatusCode')
            if HTTPStatusCode == None:
                # This should never happen unless they changed the response
                raise KeyError("aws_lambda.trigger_event: HTTPStatusCode not found!")
            else:
                if HTTPStatusCode == 202:
                    # All went well
                    triggerSuccess = True
                else:
                    # Again with the issues!
                    print("aws_lambda.trigger_event: received unexpected response code {}!".format(HTTPStatusCode))

    return(triggerSuccess)