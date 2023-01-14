from django.shortcuts import render, redirect
from .models import Schedule
from .forms import QuoteForm
from django.contrib.auth.decorators import login_required
from .utils import format_date_time


# Create your views here.

@login_required(login_url='login')
def create_quote (request): 
    form = QuoteForm()
    profile = request.user.profile
    if request.method == "POST":
        print(request.POST)
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.owner = profile
            quote.save()
            if request.POST['date_time']:
                Schedule.objects.create(
                    time_tag = format_date_time(request.POST['date_time']), 
                    quote_owner = quote)
            return redirect('profile', profile.username)
        else:
            print(form.errors)  
    context = {'form': form}
    return render(request, 'quotes/quotes.html', context)

@login_required(login_url='login')
def update_quote (request, pk):
    profile = request.user.profile
    quote = profile.quote_set.get(id=pk)
    current_schedule = quote.schedule_set.all()
    form = QuoteForm(instance=quote)
    if request.method == "POST":
        form = QuoteForm(request.POST)
        form.is_valid()
        form.save()
        if request.POST['date_time']:
            print(type(request.POST['date_time']))
            Schedule.objects.create(
                time_tag = format_date_time(request.POST['date_time']), 
                quote_owner = quote)
    context = {'form': form, 'schedule': current_schedule, 'quote': quote}
    return render(request, 'quotes/quotes.html', context)


@login_required(login_url='login')
def delete_time_tag(request, pkq, pktt):
    profile = request.user.profile
    quote = profile.quote_set.get(id=pkq)
    time_tag = quote.schedule_set.get(id=pktt)
    time_tag.delete()
    return redirect('update-quote', quote.id)

@login_required(login_url='login')
def delete_quote(request, pk):
    profile = request.user.profile
    quote = profile.quote_set.get(id=pk)
    quote.delete()
    return redirect('profile', profile.username)