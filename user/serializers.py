"""Serializers for user registration, admin registration"""

from dataclasses import field
from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model


USER = get_user_model()


class UserRegistrationSerializers(serializers.ModelSerializer):
    """User registration serializers, fields-> email, name, password """

    class Meta:
        model = USER
        fields = ['email','name','password']
    
    def create(self, attrs):
        user = User.objects.create_user(
            email=attrs['email'],
            name=attrs['name'],
            password=attrs['password']
        )
        user.save()
        
        return user


class AdminRegistrationSerializer(serializers.ModelSerializer):
    """Admin registration serializers, fields-> email, name, password """

    class Meta:
        model = USER
        fields = ['email','name','password']

    def create(self, attrs):
        user = User.objects.create_superuser(
            email=attrs['email'],
            name=attrs['name'],
            password=attrs['password']
        )
        user.save()
        
        return user
