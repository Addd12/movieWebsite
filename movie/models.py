from django.db import models
from django.utils import timezone

# Create your models here.

class Movie(models.Model):

    title = models.CharField(max_length=150)
    cast = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/thumbnail", blank=True)
    year = models.DateTimeField(default=timezone.now)
    genre = models.CharField(max_length=100)
    age_restriction = models.IntegerField()
    duration = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title #writes the title of the movie on admin page instead of movie obj
