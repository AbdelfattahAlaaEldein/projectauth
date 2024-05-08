# accounts/urls.py

from django.urls import path
from .views import   change_password, profile_detail, register_user, user_login, user_logout


urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
    
     path('profile/', profile_detail, name='profile_detail'),
]

