# awsWorks
##
### Raison d'être 
###
###### I have been coding python to explore controling AWS instances with python and I thought I would share my code as an example for those who are learning as well. 
######
### Prerequisite
###
###### - Python3 is installed: https://www.python.org/download/releases/3.0/
###### - Boto3 is installed: https://pypi.org/project/boto3/
###### - You have an AWS account: https://aws.amazon.com/resources/create-account/
###### - You have setup your AWS credenitals: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html 
######
### Programs
###
##### awsCreate
#####
###### Usage: awsCreate keypair
######
###### awsCreate takes a keypair designation as a commandline argument. If the keypair does not exist it will be created, a path to the pem file will be printed. The program will then create a Amazon Linux 2 AMI with a type of t2.micro. Got to start somewhere!
