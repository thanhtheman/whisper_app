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


