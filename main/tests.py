from django.test import TestCase
from django.urls import reverse, resolve
from .views import prompt # Replace with your actual view function

class PromptsURLTest(TestCase):
    def test_prompts_url_exists(self):
        response = self.client.get("/prompt/")
        self.assertEqual(response.status_code, 200)

    def test_prompts_url_resolves_to_correct_view(self):
        found = resolve("/prompt/")
        self.assertEqual(found.func, prompt)

    def test_prompts_url_reverse_lookup(self):
        url = reverse("prompt")
        self.assertEqual(url, "/prompt/")
