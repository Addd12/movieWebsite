from django.shortcuts import render
from django.views import generic
from .models import Movie, Comment
from .forms import CommentForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse


class MovieView(generic.ListView):
  model = Movie
  template_name = 'index.html'

def faq(request):
  return render(request, 'faq.html')

def about(request):
  return render(request, 'about.html')

class MovieDetailsView(FormMixin, DetailView):
  model = Movie
  template_name = "details.html"
  form_class = CommentForm

  def get_success_url(self):
    return reverse('details', kwargs={'pk': self.object.pk})

  def post(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return HttpResponseForbidden()
    self.object = self.get_object()
    form = self.get_form()
    if form.is_valid():
      return self.form_valid(form)
    else:
      return self.form_invalid(form)

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.movie = self.object
    form.save()
    return super().form_valid(form)

    