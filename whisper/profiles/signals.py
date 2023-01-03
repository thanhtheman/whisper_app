from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete

def create_profile(sender, instance, created, **kwargs):
    if created:
        print('a new user is created')
        user = instance
        Profile.objects.create(
            user = user,
            username = user.username,
            name = user.first_name,
            email = user.email)

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