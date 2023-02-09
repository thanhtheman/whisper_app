from django.shortcuts import render, redirect
from .models import Schedule
from .forms import QuoteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import format_date_time, check_phone_number, add_time_tag_dynamodb, delete_time_tag_dynamodb

@login_required(login_url='login')
def create_quote (request): 
    form = QuoteForm()
    profile = request.user.profile
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.owner = profile
            quote.save()
            if request.POST['date_time']:
                time = format_date_time(request.POST['date_time'])
                new_time_tag = Schedule.objects.create(
                    time_tag = time[0],
                    format_time_tag=time[1], 
                    quote_owner = quote)
                add_time_tag_dynamodb(profile, new_time_tag.id, new_time_tag.format_time_tag, quote.content)
                messages.success(request, "Schedule is successfully updated.")
            return redirect('profile', profile.username)
        else:
            print(form.errors)
    if check_phone_number(profile) == True:
        try:
            phone = profile.phone_set.all()
            phone_number = phone[0].phone_number
            context = {'form': form, 'phone_number': phone_number, 'profile': profile}
        except Exception:
            print(Exception)
    else:
        context = {'form': form, 'profile': profile}
    return render(request, 'quotes/quotes.html', context)

@login_required(login_url='login')
def update_quote (request, pk):
    profile = request.user.profile
    quote = profile.quote_set.get(id=pk)
    current_schedule = quote.schedule_set.all()
    form = QuoteForm(instance=quote)
    if request.method == "POST":
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            quote = form.save()
            if request.POST['date_time']:
                time = format_date_time(request.POST['date_time'])
                if request.POST['date_time']:
                    time = format_date_time(request.POST['date_time'])
                    new_time_tag = Schedule.objects.create(
                        time_tag = time[0],
                        format_time_tag=time[1], 
                        quote_owner = quote)
                    add_time_tag_dynamodb(profile, new_time_tag.id, new_time_tag.format_time_tag, quote.content)
                messages.success(request, "Quote is successfully updated.")
        else:
            print(form.errors)
    if check_phone_number(profile) == True:
        try:
            phone = profile.phone_set.all()
            phone_number = phone[0].phone_number
            context = {'form': form, 'schedule': current_schedule, 'quote': quote, 'phone_number': phone_number, 'profile': profile}
        except Exception:
            print(Exception)
    else:
        context = {'form': form, 'schedule': current_schedule, 'quote': quote, 'profile': profile}
    return render(request, 'quotes/quotes.html', context)

@login_required(login_url='login')
def delete_time_tag(request, pkq, pktt):
    profile = request.user.profile
    quote = profile.quote_set.get(id=pkq)
    time_tag = quote.schedule_set.get(id=pktt)
    time_tag.delete()
    delete_time_tag_dynamodb(profile, pktt)
    return redirect('update-quote', quote.id)

@login_required(login_url='login')
def delete_quote(request, pk):
    profile = request.user.profile
    quote = profile.quote_set.get(id=pk)
    quote.delete()
    return redirect('profile', profile.username)