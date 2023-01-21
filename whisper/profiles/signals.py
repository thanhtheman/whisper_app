from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail
from django.conf import settings

def create_profile(sender, instance, created, **kwargs):
    if created:
        print('a new user is created')
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            name = user.first_name,
            email = user.email)
        
        subject = 'Welcome to Whisper'
        message = f'Hi {user.username},\n\nThis is Thanh, the creator of Whisper app. I am glad you are here!\n \nYou can start your journey to build new habits with our powerful self-messaging tool by logging in and adding your phone number.\n\n http://127.0.0.1:8000/login/ \n \nBe Your Own Biggest Fan!\n\nCheers,\n\nThanh - Creator of Whisper App.'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

def update_user(sender, instance, created, **kwargs):
    print('a profile is updated!')
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

    

def delete_user(instance, **kwargs):
    user = instance.user
    print('a user is deleted')
    user.delete()

post_save.connect(create_profile, sender=User) # whenever a user is created, a corresponding profile should be created
post_save.connect(update_user, sender=Profile) # whenever a profile is updated, the corresponding user should be updated
post_delete.connect(delete_user, sender=Profile) # whenever a profile is deleted, the corresponding user shoudl be deleted.