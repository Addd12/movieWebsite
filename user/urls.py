from django.urls import path
from .views import *

urlpatterns=[
    #path("profile/", profile, name='profile')
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile')
]