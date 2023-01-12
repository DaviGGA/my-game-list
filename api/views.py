from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *


class TestView(generics.CreateAPIView):
    serializer_class = TestSerializer

    def query_set(self):
        queryset= Teste.objects.all()

        return queryset

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    
