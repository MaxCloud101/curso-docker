# This file calculate how much spend a user by date, the file contain the date
import boto3
import os

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')


bucket = os.environ['S3_BUCKET']
key = os.environ['S3_KEY']

print(bucket)
print(key)

s3.download_file(bucket, key, key)

date = key.split('.')
date = date[0]

file1 = open(key, 'r')
Lines = file1.readlines()
 
list_user_id = []
list_spend_by_user = []

for line in Lines:

    if line[-1] == '\n':
        line = line[:-1]
        
    raw =line.split(',')
    
    if raw[0] != 'user_id':
        user_id = raw[0]
        if user_id not in list_user_id:
            list_user_id.append(user_id)
            list_spend_by_user.append(int(raw[2]))
        
        else:
            position = list_user_id.index(user_id)
            list_spend_by_user[position] = list_spend_by_user[position] + int(raw[2])

print(list_user_id)
print(list_spend_by_user)

table = dynamodb.Table('Sales')

with table.batch_writer() as writer:
    for (user_id, spend_by_user) in zip(list_user_id, list_spend_by_user):
        print(date)
        
        writer.put_item(Item={
            'date': date,
            'user_id': user_id,
            'spend': spend_by_user
        })
