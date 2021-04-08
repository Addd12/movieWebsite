from django.urls import path

from .views import *

urlpatterns = [
    path("", MovieView.as_view(), name="home")
]