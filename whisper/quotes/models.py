from django.db import models
import uuid
from profiles.models import Profile
from datetime import datetime


# Create your models here.
class Quote(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField(max_length=1000, null=True, blank=False)
    author = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    # it should be CharField to be compatible with flatpickr
    date_time = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
    class Meta:
        ordering =['created']

class Schedule(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    quote_owner = models.ForeignKey(Quote, null=True, blank=True, on_delete=models.CASCADE)
    time_tag = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        schedule = f'{self.quote_owner} ----- Delivery: {self.time_tag} '
        return schedule
