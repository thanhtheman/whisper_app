from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to="images/", default="images/default_profile_img.png")
    headline = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)

class Phone(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    phone_number = models.CharField(max_length=13, blank=True, null=True, unique=True, validators=[RegexValidator(r'^\d\d\d-\d\d\d-\d\d\d\d')])
    consent = models.BooleanField(blank=True, null=True)
    phone_owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone_number