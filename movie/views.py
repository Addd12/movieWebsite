from django.shortcuts import render
from django.views import generic
from .models import Movie

# Create your views here.


class MovieView(generic.ListView):
    model = Movie
    template_name = 'index.html'

def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')

def details(request):
    return render(request, 'details.html')
