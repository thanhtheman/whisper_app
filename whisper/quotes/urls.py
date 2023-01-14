from django.urls import path
from . import views

urlpatterns = [
    path('create-quote', views.create_quote, name='create-quote'),
    path('update-quote/<str:pk>/', views.update_quote, name='update-quote'),
    path('delete-time-tag/<str:pkq>/<str:pktt>/', views.delete_time_tag, name='delete-time-tag'),
    path('delete_quote/<str:pk>/', views.delete_quote, name='delete-quote')
]