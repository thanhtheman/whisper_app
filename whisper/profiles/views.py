from django.shortcuts import render

quotes = {
    'quote': 'The way to get started is to quit talking and start doing.',
    'author': 'Walt Disney'
}

def home(request):
    context = quotes
    return render(request, 'profiles/home.html', context)