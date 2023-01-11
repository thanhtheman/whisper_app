from django.urls import path
from . import views

urlpatterns = [
    path('create-quote', views.create_quote, name='create-quote'),
    path('update-quote/<str:pk>/', views.update_quote, name='update-quote')
]