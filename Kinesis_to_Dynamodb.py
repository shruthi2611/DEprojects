import json
import base64
import boto3

from datetime import datetime

def lambda_handler(event, context):

    client = boto3.client('dynamodb')
    for record in event['Records']:
        t_record = base64.b64decode(record['kinesis']['data'])
        str_record = str(t_record,'utf-8')
        dict_record = json.loads(str_record)
        customer_key = dict()
        customer_key.update({'CustomerID': {"N": str(dict_record['CustomerID'])}})
        ex_customer = dict()
        ex_customer.update({str(dict_record['InvoiceNo']): {'Value':{"S":'Some overview JSON for the UI goes here'},"Action":"PUT"}})

        response = client.update_item(TableName='Customer', Key = customer_key, AttributeUpdates = ex_customer)
        inventory_key = dict()
        inventory_key.update({'InvoiceNo': {"N": str(dict_record['InvoiceNo'])}})
