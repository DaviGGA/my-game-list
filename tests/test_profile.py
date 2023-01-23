from user.models import User, Profile
from django.urls import reverse
from unittest import TestCase
import pytest
from rest_framework.test import APIClient

class UserTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        url = reverse('register')

        data = {
            'email' : 'johntest@hotmail.com',
            'password' : 'testy1234',
            'password2' : 'testy1234'
        }

        data2 = {
            'email' : 'marytest@hotmail.com',
            'password' : 'testy1234',
            'password2' : 'testy1234'
        }

        create_user = self.client.post(url,data)
        create_user2 = self.client.post(url,data2)
        
        self.user = User.objects.get(email='johntest@hotmail.com')
        self.user2 = User.objects.get(email='marytest@hotmail.com')

    
    @pytest.mark.django_db
    def get_token(self):
        token_url = "/usuario/token/"
        payload = {'email' : 'johntest@hotmail.com', 'password' : 'testy1234'}
        response_token =self.client.post(token_url,payload)
        token = response_token.data
 
        return token

    @pytest.mark.django_db
    def test_get_all_profiles(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"

        url = reverse('profiles')
        response = self.client.get(url,HTTP_AUTHORIZATION=header, format='json')

        assert response.status_code == 200
    
    @pytest.mark.django_db
    def test_get_profile_by_id(self):
        profile = self.user.pk
        token = self.get_token()
        header = f"Bearer {token['access']}"

        url = f'/usuario/perfil/{profile}/'
        response = self.client.get(url,HTTP_AUTHORIZATION=header, format='json')

        assert response.status_code == 200


    @pytest.mark.django_db
    def test_patch_edit_profile(self):
        profile = self.user.pk
        token = self.get_token()
        header = f"Bearer {token['access']}"

        data = {
            'name' : 'John Test',
            'bio' : "I'm John Test!",
        }

        url = f'/usuario/editar-perfil/{profile}/'
        response = self.client.patch(url,data,HTTP_AUTHORIZATION=header, format='json')

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_put_edit_profile(self):
        profile = self.user.pk
        token = self.get_token()
        header = f"Bearer {token['access']}"

        data = {
            'name' : 'John Test',
            'bio' : "I'm John Test!",
            'user' : self.user.pk
        }

        url = f'/usuario/editar-perfil/{profile}/'
        response = self.client.put(url,data,HTTP_AUTHORIZATION=header, format='json')

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_update_profile_that_isnt_yours(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"

        data = {
            'name' : 'Mary Test',
            'bio' : "I'm John and i'm editing Mary's profile",
        }

        url = f'/usuario/editar-perfil/{self.user2.pk}/'
        response = self.client.patch(url,data,HTTP_AUTHORIZATION=header, format='json')

        assert response.status_code == 400

    