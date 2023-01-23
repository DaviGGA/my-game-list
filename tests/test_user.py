from user.models import User
from django.urls import reverse
from unittest import TestCase
import pytest
from rest_framework.test import APIClient

class UserTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.test_user = User.objects.create(
            username = 'John Test',
            password = 'testy1234',
            email = 'johntest@hotmail.com',
        )

    @pytest.mark.django_db
    def test_post_user(self):
        url = reverse('register')
        data = {
            'email' : 'marytest@hotmail.com',
            'password' : 'testy1234',
            'password2' : 'testy1234',
        }

        response = self.client.post(url,data)
        assert response.status_code == 201
    
    @pytest.mark.django_db
    def test_post_user_with_unmatching_passwords(self):
        url = reverse('register')
        data = {
            'email' : 'marytest@hotmail.com',
            'password' : 'testy1234',
            'password2' : 'dontmatch1234',
        }

        response = self.client.post(url,data)
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_post_user_with_password_less_than_8_characters(self):
        url = reverse('register')
        data = {
            'email' : 'marytest@hotmail.com',
            'password' : 'testy12',
            'password2' : 'testy12',
        }

        response = self.client.post(url,data)
        assert response.status_code == 400
    
    @pytest.mark.django_db
    def test_post_user_with__password_without_any_number(self):
        url = reverse('register')
        data = {
            'email' : 'marytest@hotmail.com',
            'password' : 'testytesty',
            'password2' : 'testytesty',
        }

        response = self.client.post(url,data)
        assert response.status_code == 400

    