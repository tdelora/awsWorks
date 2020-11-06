import boto3

def put_lambda_event(ruleName,scheduleExpression,arn,id):
    client = boto3.client('events')
    returnCode = False

    response = aws_put_rule(ruleName,scheduleExpression)

    if response:
        response = aws_put_targets(ruleName,arn,id)
        if response:
            returnCode = True
    
    return returnCode

def delete_lambda_event():
    client = boto3.client('events')

    pass

def aws_put_rule(ruleName,scheduleExpression):
    client = boto3.client('events')
    returnCode = False

    response = client.put_rule(Name=ruleName,ScheduleExpression=scheduleExpression,State='ENABLED')

    httpStatusCode = getHttpsStatusCode(response)
    if httpStatusCode == 200:
            # All went well
            returnCode = True
    else:
            print("aws_event.aws_put_rule: received unexpected http status code {}" % httpStatusCode)

    return returnCode

def aws_enable_rule(ruleName):
    client = boto3.client('events')

    pass

def aws_disable_rule(ruleName):
    client = boto3.client('events')

    pass

def aws_delete_rule(ruleName):
    client = boto3.client('events')
    
    pass

def aws_put_targets(ruleName,arn,id):
    client = boto3.client('events')
    returnCode = False

    targetsList = [{"Arn":"arn:aws:lambda:us-west-1:985167159610:function:term-running-ec2-instances","Id":"term-running-ec2-instances"}]
    response = client.put_targets(Rule=ruleName,Targets=targetsList)

    httpStatusCode = getHttpsStatusCode(response)
    if httpStatusCode == 200:
            # All went well
            returnCode = True
    else:
            print("aws_event.aws_put_targets: received unexpected http status code {}" % httpStatusCode)

    return returnCode

def aws_remove_target(ruleName,id):
    client = boto3.client('events')
    
    pass

def getHttpsStatusCode(response):
    returnStatusCode = 404
    responseMetadata = response.get('ResponseMetadata')
    if responseMetadata:
        httpStatusCode = responseMetadata.get('HTTPStatusCode')
        if httpStatusCode:
            returnStatusCode = httpStatusCode
    else:
        print("aws_event.httpsStatusCode: Expected key ResponseMetadata not found")

    return returnStatusCode