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
###### Usage: awsCreate [-h] [-n MINCOUNT] [-x MAXCOUNT] -k KEYPAIR
######
###### awsCreate takes a keypair designation as a mandatory command line argument. If the keypair does not exist it will be created, a path to the pem file will be printed. Optionally the user may specify the minimum and maximum number of instances to start. The program will then create the specified numer of Amazon Linux 2 AMI instances with a type of t2.micro. 
#####
##### awsTerminate
#####
###### Usage: awsTerminate [-h] [-i ID] [-a]
######
###### awsTerminate will terminate running (state 16) AWS instances. With the --id (or -i) you can specify the instance or with --all (or -a) all running instances will be terminated without prompting the user.
