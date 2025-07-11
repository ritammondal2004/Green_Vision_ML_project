import  boto3
import os
from dotenv import load_dotenv
load_dotenv()  

class S3Client:
    
    S3_client, S3_resource = None, None

    def __init__(self, region_name=os.environ['AWS_DEFAULT_REGION']):

        if S3Client.S3_resource==None or S3Client.S3_client==None:
            __access_key_id = os.environ['AWS_ACCESS_KEY_ID']
            __secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

            if __access_key_id is None:
                raise Exception("Environment variable: AWS_ACCESS_KEY_ID is not set.") 
            if __secret_access_key is None:
                raise Exception("Environment variable: AWS_SECRET_ACCESS_KEY is not set.") 
            
            S3Client.S3_resource = boto3.resource('s3',
                                              aws_access_key_id = __access_key_id,
                                              aws_secret_access_key = __secret_access_key,
                                              region_name = region_name) 
            S3Client.S3_client = boto3.client('s3',
                                              aws_access_key_id = __access_key_id,
                                              aws_secret_access_key = __secret_access_key,
                                              region_name = region_name
                                              )  
            
        self.S3_client = S3Client.S3_client
        self.S3_resource = S3Client.S3_resource 
            
 