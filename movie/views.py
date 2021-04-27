from django.shortcuts import render
from django.views import generic
from .models import Movie, Comment
from .forms import CommentForm


class MovieView(generic.ListView):
  model = Movie
  template_name = 'index.html'

def faq(request):
  return render(request, 'faq.html')

def about(request):
  return render(request, 'about.html')

class MovieDetailsView(generic.DetailView):
  model = Movie
  template_name = "details.html"

# class AddCommentView(generic.CreateView):
#     model = Comment
#     template_name = "details.html"
#     fields = '__all__'

def comment(request, id):
    
  if request.method == 'POST':
    cf = CommentForm(request.POST or None)
    if cf.is_valid():
      content = request.POST.get('content')
      comment = Comment.objects.create(post = post, user = request.user, content = content)
      comment.save()
      return redirect(post.get_absolute_url())
    else:
      cf = CommentForm()
        
    context ={
      'comment_form':cf,
      }
    return render(request, 'details.html', context)
    