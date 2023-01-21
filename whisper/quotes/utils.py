import datetime

def format_date_time(date_time):
    date, time = date_time.split(' ')
    year, month, day = date.split('-')
    x = datetime.datetime(int(year), int(month), int(day))
    format_month = x.strftime('%B')
    format_day = x.strftime('%d')
    format_year = x.strftime('%Y')
    format_datetime = f'{format_month} {format_day}, {format_year} @ {time}'
    return format_datetime

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
def add_time_tags(profile):
    try:
        if check_phone_number(profile) == True:
            quotes = profile.quote_set.all()
            for quote in quotes:
                scheduled_time_tags = quote.schedule_set.all()
                for tag in scheduled_time_tags:
                    # this will be replaced by the add_to_dynamodb()
                    with open('time_tag.txt','w') as file:
                        file.write(f'{tag.quote_owner}: {tag.time_tag}')
            print('Time tags are successfully added to DynamoDB')
    except Exception:
        print(Exception)
    

