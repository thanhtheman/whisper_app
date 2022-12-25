from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_quotes, name='create-quote')
]