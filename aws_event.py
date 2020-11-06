import boto3

def put_lambda_event(ruleName,scheduleExpression,arn,id):
    client = boto3.client('events')
    returnCode = False

    response = aws_put_rule(ruleName,scheduleExpression)

    if response:
        response = aws_put_target(ruleName,arn,id)
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

    print(response)
    returnCode = True

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

def aws_put_target(ruleName,arn,id):
    client = boto3.client('events')
    returnCode = False
    
    return returnCode

def aws_remove_target(ruleName,id):
    client = boto3.client('events')
    
    pass