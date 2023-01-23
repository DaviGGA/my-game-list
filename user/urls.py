from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path ('testes/', TestView.as_view(), name ='testes'),
    path('registro/', UserRegisterView.as_view(), name = 'register'),
    path('editar-perfil/<str:pk>/', ProfileEditView.as_view(), name = 'edit-profile'),
    path('perfis/', ProfileListView.as_view(), name = 'edit-profile'),
    path('perfil/<str:pk>/', ProfileView.as_view(), name = 'edit-profile'),
    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name = 'token_refresh'),
]