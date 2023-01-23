from django.shortcuts import render
from django.db.models import Q
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny,IsAuthenticated


class TestView(generics.CreateAPIView):
    serializer_class = TestSerializer
    permission_classes = (AllowAny,)

    def query_set(self):
        queryset= Teste.objects.all()

        return queryset

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)
    
class ProfileEditView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        queryset = Profile.objects.filter(pk = self.kwargs['pk'])
        return queryset
    
class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Profile.objects.all()
        search_content = self.request.query_params.get('search')
        
        if search_content is not None:
            queryset = Profile.objects.filter(Q(name__icontains = search_content) | Q(user__username__icontains=search_content))
        
        return queryset

class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        queryset = Profile.objects.filter(pk = self.kwargs['pk'])
        return queryset