from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from movie.views import about, faq


class TestAboutPage(TestCase):
    def test_uses_about_template(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_about_returns_correct_html(self):
        request = HttpRequest()
        response = about(request)
        self.assertIn(b"<title>About</title>", response.content)
        self.assertTrue(response.content.endswith(b"</html>"))


class TestFaqPage(TestCase):
    def test_uses_faq_template(self):
        response = self.client.get(reverse("faq"))
        self.assertTemplateUsed(response, "faq.html")

    def test_faq_returns_correct_html(self):
        request = HttpRequest()
        response = faq(request)
        self.assertIn(b"<title>FAQ</title>", response.content)
        self.assertTrue(response.content.endswith(b"</html>"))
