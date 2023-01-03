from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

quotes = {
    'quote': 'The way to get started is to quit talking and start doing.',
    'author': 'Walt Disney'
}

def home(request):
    context = quotes
    return render(request, 'profiles/home.html', context)


def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        redirect('profiles')

    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or Password is incorrect!')
    context = {'page': page}
    return render(request, 'profiles/login_register.html', context)

def logout_user(request):
    logout(request)
    messages.info(request,'You have successfully logged out.')
    return redirect('profiles')

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
            return redirect('profiles')
        else:
            messages.error(request, "An error has occured, please check username & password requirements.")
    context = {'form': form, 'page': page}
    return render(request, 'profiles/login_register.html', context)