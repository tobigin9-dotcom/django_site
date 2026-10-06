from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class RegisterViewTestCase(TestCase):
    def test_register_creates_user_and_profile(self):
        response = self.client.post(
            reverse('myauth:register'),
            {
                "username": "newuser",
                "password1": "S3cure-pass-123",
                "password2": "S3cure-pass-123",
            },
        )
        self.assertRedirects(response, reverse('myauth:about-me'))
        user = User.objects.get(username="newuser")
        self.assertTrue(Profile.objects.filter(user=user).exists())
