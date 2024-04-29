import json
import boto3  
import time
import datetime

REGION="us-east-1"
dynamodb = boto3.resource('dynamodb',region_name=REGION)
table = dynamodb.Table('PhotoGallery')

def lambda_handler(event, context):
    photoID = str(event['body-json']['PhotoID'])
    creationTime = int(event['body-json']['CreationTime'])
    title=str(event['body-json']['title'])
    description=str(event['body-json']['description'])
    tags=str(event['body-json']['tags'])


    table.update_item(
        Key = {"PhotoID": photoID, "CreationTime": creationTime},
        ExpressionAttributeValues = {
            ':title': title, ':description': description, ':tags': tags
        },
        UpdateExpression = 'set Title = :title, Description = :description, Tags = :tags'
    );

    return {
        "statusCode": 200,
        "body": {json.dumps(photoID), json.dumps(creationTime), json.dumps(title),
                 json.dumps(description), json.dumps(tags)}
    }

