import boto3
import json

def lambda_handler(event, context):
    method = event['context']['http-method']
    if method =="GET":
        dynamo_client = boto3.client('dynamodb')
        im_invid = event['params']['querystring']['InvoiceNo']
        response = dynamo_client.get_item(TableName ='Invoice', Key = {'InvoiceNo':{'N':im_invid}})
        
      

        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])}
    elif method == 'POST':
        p_record=event['body-json']
        recordstring=json.dumps(p_record)
        client=boto3.client('kinesis')
        response=client.put_record(
            StreamName='Apidata',
            Data=recordstring,
            PartitionKey='string'
        )
    return {
        'statusCode': 200,
        'body': json.dumps(p_record)
    }
