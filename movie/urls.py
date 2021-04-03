from django.urls import path

from .views import *

urlpatterns = [
    path("", movie, name="home")
]