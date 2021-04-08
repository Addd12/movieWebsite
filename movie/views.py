from django.shortcuts import render
from django.views import generic
from .models import Movie

# Create your views here.

# def movie(request):
#     return render(request, 'movie.html')

class MovieView(generic.ListView):
    model = Movie
    template_name = 'movie.html'
