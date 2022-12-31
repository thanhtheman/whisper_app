from django.shortcuts import render
from .models import Quote
from .forms import QuoteForm
from pytz import timezone
import datetime
from whisper import settings
# Create your views here.


def create_quotes (request):
    quote = Quote.objects.first()
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST['date'])
            print(request.POST['time'])
            # user_timezone = datetime.datetime(2022, 12, 26)
            # time_zone = user_timezone.tzinfo
            # conversion = user_timezone.astimezone(timezone(settings.TIME_ZONE))
            # print(time_zone)
            # print(conversion)
        else:
            print(form.errors)
    
    form = QuoteForm
    context = {'quote': quote, 'form': form}
    return render(request, 'quotes/quotes.html', context)



