import json
import csv
import boto3

def lambda_handler(event, context):
    region = 'eu-west-2'
    record_list = []
    
    try:
        s3 = boto3.client('s3')
        dynamodb = boto3.client('dynamodb', region_name=region)
        
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        print('Bucket: ', bucket, '--- Key: ', key)
        csv_file = s3.get_object(Bucket = bucket, Key = key)
        record_list = csv_file['Body'].read().decode('utf-8').split('\n')
        
        csv_reader = csv.reader(record_list, delimiter = ',', quotechar='"')
        next(csv_reader)
        
        i = 0 
        for row in csv_reader:
            song_id = row[0]
            artist = row[1]
            song = row[2]
            topic = row[3]
            i+=1
            print(i, 'Aritst: ', artist,'Song: ', song, 'Topic: ', topic)   
            add_to_db = dynamodb.put_item(
                TableName = 'test2',
                Item={
                    'song_id': {'S': str(song_id)},
                    'artist': {'S': str(artist)},
                    'song': {'S': str(song)},
                    'topic':  {'S': topic}})
            print('Successful Addedd to dynamodb')   
    except Exception as e:
        print(str(e))
    
    return {
        'statusCode': 200,
        'body': json.dumps('CSV to DynamoDv success')
    }
