import boto3

def aws_session(role_arn=None, session_name='my_session'):

    if role_arn:
        client = boto3.client('sts')
        response = client.assume_role(RoleArn=role_arn, RoleSessionName=session_name)
        session = boto3.Session(
            aws_access_key_id=response['Credentials']['AccessKeyId'],
            aws_secret_access_key=response['Credentials']['SecretAccessKey'],
            aws_session_token=response['Credentials']['SessionToken'])
        return session
    else:
        return boto3.Session()

def lambda_handler(event, context):
    master_role_arn = os.environ['MASTER_ROLE_ARN']
    session_assumed = aws_session(role_arn=master_role_arn, session_name='my_lambda')
    session_regular = aws_session()
  
    print(session_assumed.client('sts').get_caller_identity()['Account'])
    print(session_regular.client('sts').get_caller_identity()['Account'])
