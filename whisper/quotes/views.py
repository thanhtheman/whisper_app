from django.shortcuts import render
from .models import Quote
# Create your views here.
def create_quotes (request):
    quote = Quote.objects.first()
    context = {'quote': quote}
    return render(request, 'quotes/quotes.html', context)