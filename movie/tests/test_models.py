from django.test import TestCase
from movie.models import Movie


class TestMovies(TestCase):
    def test_movie_string_representation(self):
        movie = Movie(title="Movie title")
        self.assertEqual(str(movie), movie.title)
