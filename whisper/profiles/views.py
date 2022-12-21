from django.shortcuts import render

# Create your views here.
def get_profiles(request):
    context = {'name': 'Thanh Quach'}
    return render(request, 'profiles/profiles.html', context)