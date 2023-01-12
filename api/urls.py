from django.urls import path
from .views import *

urlpatterns = [
    path ('testes', TestView.as_view(), name ='testes'),
    path('registro/', UserRegisterView.as_view(), name = 'register')
]