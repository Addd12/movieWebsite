from django.urls import path

from .views import *

urlpatterns = [
    path("", MovieView.as_view(), name="home"),
    path("faq/", faq, name="faq"), 
    path("about/", about, name="about"), 
    path("details/<int:pk>", MovieDetailsView.as_view(), name="details"),
]