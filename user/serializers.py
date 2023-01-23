from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
import re

from django.contrib.auth.password_validation import validate_password


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teste
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True,required = True)

    class Meta:
        model = User
        fields = ['email','password','password2']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
    
    def validate(self,data):

        digits = "[0-9]"
        password_has_numbers = re.search(digits, data['password'])

        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password_match': 'As senhas não coincidem.'}
            )
        if len(data['password']) < 8:
            raise serializers.ValidationError(
                {'password_length' : 'Sua senha deve conter pelo menos 8 caracteres.'}
            )

        if not password_has_numbers:
            raise serializers.ValidationError(
                {'password' : 'Sua senha deve contar pelo menos 1 número'}
            )
            
        return data

    def save(self):
        user = User.objects.create(
            email = self.validated_data['email'],
        )
        user.set_password(self.validated_data['password'])
        user_id = str(user.id)
        user.username = f"Username{user_id.zfill(5)}"
        user.save()

        user_profile = Profile.objects.create(user=user)
        user_profile.save()

        return user,user_profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {
            'email' : {'read_only' : True}
        }
    
    def update(self,instance):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError(
                {'authorization' : "You don't have permission to update this user"}
            )

        instance.save()

        return instance

