from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import boto3

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
    sns_client = boto3.client('sns')
    response = sns_client.create_sms_sandbox_phone_number(
        PhoneNumber=phone_number,
        LanguageCode='en-US'
    )
    print("A new phone number has been added: \n" + response)

def verify_sms_phone_number(phone_number, one_time_passcode):
    sns_client=boto3.client('sns')
    response = sns_client.verify_sms_sandbox_phone_number(
        PhoneNumber=phone_number,
        OneTimePasscode=one_time_passcode
    )
    print("Phone Number is successfully verified! \n" + response)