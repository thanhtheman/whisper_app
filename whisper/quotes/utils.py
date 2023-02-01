import datetime
import boto3
import os
from dotenv import load_dotenv
load_dotenv()
from profiles.utils import convert_phone_number

def format_date_time(date_time):
    date, time = date_time.split(' ')
    hour, minute = time.split(':')
    second ='00'
    year, month, day = date.split('-')
    x = datetime.datetime(int(year), int(month), int(day))
    display_month = x.strftime('%B')
    format_month = x.strftime('%m')
    format_day = x.strftime('%d')
    format_year = x.strftime('%Y')
    display_datetime = f'{display_month} {format_day}, {format_year} @ {time}'
    format_datetime = f'at({format_year}-{format_month}-{format_day}T{hour}:{minute}:{second})'
    return [display_datetime, format_datetime]

# situation 1: this will ensure current users will add all the time tags to dynamoDB
# situation 2: for new user, we will integrate this into the get_phone_number function
def check_phone_number(profile):
    try:
        phone = profile.phone_set.all()
        phone_number = phone[0].phone_number
        if phone_number:
            return True
    except Exception:
        print(Exception)

# this will replace the time_tag.txt file
def first_time_add_time_tags_dynamodb(profile):
    try:
        if check_phone_number(profile) == True:
            quotes = profile.quote_set.all()
            for quote in quotes:
                scheduled_time_tags = quote.schedule_set.all()
                for tag in scheduled_time_tags:
                    add_time_tag_dynamodb(profile, tag.id, tag.format_time_tag, quote.content)
                    print(f'{tag.id} is successfully added to DynamoDB')
    except Exception:
        print(Exception)
    
def add_time_tag_dynamodb(profile, time_tag_id, format_time_tag, quote_content):
    try:
        if check_phone_number(profile) == True:
            phone = profile.phone_set.all()
            phone_number = phone[0].phone_number
            format_phone_number = convert_phone_number(phone_number)
            dynamodb_client = boto3.client('dynamodb')
            table_name = os.getenv('DYNAMODB_TABLE_NAME')
            response = dynamodb_client.put_item(
                TableName= table_name,
                Item={
                    'time_tag_id': {'S': str(time_tag_id)},
                    'username':{'S': profile.username},
                    'phone_number':{'S':format_phone_number},
                    'format_time_tag':{'S': format_time_tag},
                    'quote_message': {'S': quote_content},
                }
            )
            print(response)
    except (dynamodb_client.exceptions.ConditionalCheckFailedException,
            dynamodb_client.exceptions.ProvisionedThroughputExceededException,
            dynamodb_client.exceptions.ResourceNotFoundException,
            dynamodb_client.exceptions.ItemCollectionSizeLimitExceededException,
            dynamodb_client.exceptions.TransactionConflictException,
            dynamodb_client.exceptions.RequestLimitExceeded,
            dynamodb_client.exceptions.InternalServerError) as e:
        print(e)
