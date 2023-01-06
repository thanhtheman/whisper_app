from django.shortcuts import render, redirect
from .models import Schedule
from .forms import QuoteForm
from pytz import timezone

# Create your views here.


def create_quote (request): 
    form = QuoteForm()
    if request.method == "POST":
        print(request.POST)
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save()
            if request.POST['date_time']:
                Schedule.objects.create(
                    time_tag = request.POST['date_time'], 
                    quote_owner = quote)
            return redirect('home')
        else:
            print(form.errors)  
    context = {'form': form}
    return render(request, 'quotes/quotes.html', context)



