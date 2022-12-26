from django.shortcuts import render
from .models import Quote
from .forms import QuoteForm
# Create your views here.
def create_quotes (request):
    quote = Quote.objects.first()
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            print(request.POST['content'])
            print(request.POST['date'])
            print(request.POST['time'])
        else:
            print(form.errors)
    
    form = QuoteForm
    context = {'quote': quote, 'form': form}
    return render(request, 'quotes/quotes.html', context)