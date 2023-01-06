from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register_user, name='user_registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')

]