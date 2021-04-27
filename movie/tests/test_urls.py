from django.test import TestCase
from django.urls import resolve, reverse
from movie.views import about, faq


class TestUrls(TestCase):
    def test_about_page_url(self):
        url = reverse("about")
        self.assertEquals(resolve(url).func, about)

    def test_faq_page_url(self):
        url = reverse("faq")
        self.assertEquals(resolve(url).func, faq)
