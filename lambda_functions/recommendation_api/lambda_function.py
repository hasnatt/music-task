import json
from boto3.dynamodb.conditions import Key, Attr
import boto3

def lambda_handler(event, context):
    
    #1. Parse out query string params
    artist= event['queryStringParameters']['artist'].lower()
    song = event['queryStringParameters']['song'].lower()
    amount = int(event['queryStringParameters']['amount'])
    
    #2. query dynamodb
    client = boto3.resource('dynamodb')
    table = client.Table('test2')
    # response = table.scan(
    #     FilterExpression=Attr('artist').eq(artist) & Attr('song').eq(song))
    # items = response["Items"]
    
    
    response = table.get_item(
        Key={
            'song_id': f'{artist}+{song}',
        })
    queried_topic = response['Item']['topic']
    
    topic_query = table.scan(
        FilterExpression=Attr('topic').eq(queried_topic) )
    recommended_songs = topic_query
    
    
    # print(response)
    
    
    
    #3. Construct the body of the response object
    transactionResponse = {}
    transactionResponse['artist'] = artist
    transactionResponse['song'] = song
    transactionResponse['queried_topic'] = response['Item']['topic']
    transactionResponse['amount'] = amount
    transactionResponse['recommended_songs'] = recommended_songs['Items'][0:amount]
    
    #4. Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)
    #5. Return the response object
    return responseObject
