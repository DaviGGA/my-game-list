from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny,IsAuthenticated


class TestView(generics.CreateAPIView):
    serializer_class = TestSerializer
    permission_classes = (IsAuthenticated,)

    def query_set(self):
        queryset= Teste.objects.all()

        return queryset

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)
    
