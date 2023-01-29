from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('register/', views.register_user, name='user_registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('phone-number/', views.get_phone_number, name='phone'),
    path('phone-verification/', views.verify_phone_number, name='phone_verification')

]