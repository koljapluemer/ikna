from django.test import TestCase
from django.urls import reverse, resolve
from .views import prompts_view  # Replace with your actual view function

class PromptsURLTest(TestCase):
    def test_prompts_url_exists(self):
        response = self.client.get("/prompts/")
        self.assertEqual(response.status_code, 200)

    def test_prompts_url_resolves_to_correct_view(self):
        found = resolve("/prompts/")
        self.assertEqual(found.func, prompts_view)

    def test_prompts_url_reverse_lookup(self):
        url = reverse("prompts")
        self.assertEqual(url, "/prompts/")
