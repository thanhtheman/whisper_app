from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import boto3
import os
from dotenv import load_dotenv
load_dotenv()
key_id = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region = os.getenv('REGION_NAME')

def paginating (request, collection, number_of_results_per_page):
    page = request.GET.get('page')
    p = Paginator(collection, number_of_results_per_page)
    try:
        results_per_page = p.page(page)
    except PageNotAnInteger:
        page = 1
        results_per_page = p.page(page)
    except EmptyPage:
        page = p.num_pages
        results_per_page = p.page(page)

    left_index = int(page) - 1
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 2
    if right_index > p.num_pages:
        right_index = p.num_pages + 1
    custom_range = range(left_index, right_index)

    return custom_range, results_per_page

def convert_phone_number(phone_number):
    phone_number = phone_number.replace('-','')
    phone_number = '+1' + phone_number
    return phone_number

def create_sms_phone_number(phone_number):
    sns_client = boto3.client('sns',aws_access_key_id=key_id, 
    aws_secret_access_key=secret_key, region_name=region)
    error = ''
    try:
        response = sns_client.create_sms_sandbox_phone_number(
            PhoneNumber=phone_number,
            LanguageCode='en-US'
        )
    except(
        sns_client.exceptions.AuthorizationErrorException,
        sns_client.exceptions.InternalErrorException,
        sns_client.exceptions.InvalidParameterException,
        sns_client.exceptions.OptedOutException,
        sns_client.exceptions.UserErrorException,
        sns_client.exceptions.ThrottledException,
    ) as e:
        print(e)
        error = e
    if error != '':
        return 'There is an error, please check your phone number again!'
    else:
        print(response)
        return 'Your phone number has been successfully submitted.'

def verify_sms_phone_number(phone_number, one_time_passcode):
    sns_client=boto3.client('sns', aws_access_key_id=key_id, 
    aws_secret_access_key=secret_key, region_name=region)
    error = ''
    try:
       response = sns_client.verify_sms_sandbox_phone_number(
            PhoneNumber=phone_number,
            OneTimePassword=one_time_passcode
        )
    except (sns_client.exceptions.AuthorizationErrorException,
        sns_client.exceptions.InternalErrorException,
        sns_client.exceptions.InvalidParameterException,
        sns_client.exceptions.ResourceNotFoundException,
        sns_client.exceptions.VerificationException,
        sns_client.exceptions.ThrottledException,
    ) as e:
        print(e)
        error = e
    if error != '':
        return 'There is an error, please check your passcode again!'
    else:
        print(response)
        return 'Your phone number has been successfully verified.'

def subscribe_to_topic(phone_number):
    sns_client=boto3.client('sns', aws_access_key_id=key_id, 
    aws_secret_access_key=secret_key, region_name=region)
    try:
        response = sns_client.subscribe(TopicArn='arn:aws:sns:us-east-1:941349218315:Whisper', Protocol='sms', Endpoint=phone_number)
        print(f'{phone_number} was successfully subscribed.')
    except(
        sns_client.exceptions.SubscriptionLimitExceededException,
        sns_client.exceptions.FilterPolicyLimitExceededException,
        sns_client.exceptions.InvalidParameterException,
        sns_client.exceptions.InternalErrorException,
        sns_client.exceptions.NotFoundException,
        sns_client.exceptions.AuthorizationErrorException,
        sns_client.exceptions.InvalidSecurityException) as e:
            print(e)

    