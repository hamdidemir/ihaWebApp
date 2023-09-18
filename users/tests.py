from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UsersViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_view_authenticated(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send GET request to login view
        response = self.client.get(reverse('users:login'))

        # Check that the response has a 200 status code (OK)
        self.assertEqual(response.status_code, 200)


    def test_login_view_unauthenticated(self):
        # Log out any authenticated user
        self.client.logout()

        # Send GET request to login view
        response = self.client.get(reverse('users:login'))

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send GET request to logout view
        response = self.client.get(reverse('users:logout'))

        # Check that the response has a 200 status code (OK)
        self.assertEqual(response.status_code, 200)

        # Optionally, you can check the content of the response to ensure it matches
        # the content you expect in the 'users/login.html' template.
        self.assertContains(response, "Çıkış Yapıldı")

    def test_register_view(self):
        # Log out any authenticated user
        self.client.logout()

        # Send GET request to register view
        response = self.client.get(reverse('users:register'))

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)
