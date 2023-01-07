from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .utils import paginating

quotes = {
    'quote': 'The way to get started is to quit talking and start doing.',
    'author': 'Walt Disney'
}

def home(request):
    context = quotes
    return render(request, 'profiles/home.html', context)

@login_required(login_url='login')
def profile (request, username):
    profile = Profile.objects.get(username=username)
    quotes = profile.quote_set.all()
    custom_range, results_per_page = paginating(request, quotes, 3)
    context = {'profile': profile, 'results_per_page': results_per_page, 'custom_range': custom_range}
    return render(request, 'profiles/profile.html', context)

def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        redirect('profile')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile', user.username)
        else:
            messages.error(request, 'Username or Password is incorrect!')
    context = {'page': page}
    return render(request, 'profiles/login_register.html', context)

def logout_user(request):
    logout(request)
    messages.info(request,'You have successfully logged out.')
    return redirect('home')

def register_user(request):
    page = 'user_registration'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            print('a user is created')
            user.save()
            messages.success(request, 'Your account has been successfully created!')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error has occured, please check username & password requirements.")
    context = {'form': form, 'page': page}
    return render(request, 'profiles/login_register.html', context)