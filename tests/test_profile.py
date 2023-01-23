from api.models import User, Profile
from django.urls import reverse
from unittest import TestCase
import pytest
from rest_framework.test import APIClient

class UserTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.test_user = User.objects.create(
            password = 'testy1234',
            email = 'johntest@hotmail.com',
        )

        self.test_profile = Profile.objects.create(user = self.test_user)

    
    @pytest.mark.django_db
    def get_token(self):
        token_url = "/token/"
        payload = {'email' : 'johntest@hotmail.com', 'password' : 'testy1234'}
        response_token =self.client.post(token_url,payload)
        token = response_token.data
    
        return token

    