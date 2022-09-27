import base64
import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')
dateTime = datetime.now()
timestampStr = dateTime.strftime("%d-%b-%Y-%H%M%S")

kRecords = []

def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        kRecords.append(payload)
   
    ex_string = b'\n'.join(kRecords)
    mykey = 'output' + timestampStr + '.txt'
    response = s3.put_object(Body=ex_string, Bucket='<bucket name>', Key= mykey)
