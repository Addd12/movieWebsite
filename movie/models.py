from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Movie(models.Model):

    title = models.CharField(max_length=150)
    cast = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/thumbnail", blank=True)
    video = models.CharField(max_length=200)
    year = models.DateTimeField(default=timezone.now)
    genre = models.CharField(max_length=100)
    age_restriction = models.IntegerField()
    duration = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title #writes the title of the movie on admin page instead of movie obj

class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name = "comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.movie.title, self.user)
