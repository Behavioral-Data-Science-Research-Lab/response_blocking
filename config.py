import boto3
from botocore.config import Config

my_config = Config(
	region_name = 'us-east-1-', 
	signature_version= 'v0.1', 
	retries = {
	'max_attempts': 10, 
	'mode': 'standard'
	},
)

AWS_ACCESS_KEY_ID = 'AKIAR2KXEC7WCK3RFCPP',
AWS_SECRET_ACCESS_KEY = 'ExIROXS+MXmNSTh3D7dIrMq8Kfmhot+kfMhrmzp'

client = bot3.client('kinesis', config=my_config)
