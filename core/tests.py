from django.test import TestCase
from django.urls import reverse


class NavbarActiveStateTests(TestCase):
    def test_navbar_active_class_tracks_current_route(self):
        response = self.client.get(reverse('contact'))
        html = response.content.decode('utf-8')

        self.assertIn(f'class="nav-link active" href="{reverse("contact")}"',html,)
        self.assertNotIn(f'class="nav-link active" href="{reverse("home")}"',html,)
