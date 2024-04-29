import json
import boto3  
import time
import datetime

REGION="us-east-1"
dynamodb = boto3.resource('dynamodb',region_name=REGION)
table = dynamodb.Table('PhotoGallery')

def lambda_handler(event, context):
    #print("Hello")
    photoID = event['body-json']['photoid']
    creationTime = event['body-json']['creationtime']

    table.delete_item(
        Key = {"CreationTime": creationTime, "PhotoID": photoID}
        );
    
    return {
        "statusCode": 200,
        "body": json.dumps(photoID)
    }
