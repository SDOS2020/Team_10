from rest_framework import serializers
from .models import *

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'email', 'password', 'first_name', 'last_name',)

class UserSerializer(serializers.Serializer):
    class Meta:
        fields = (
            'first_name', 'email', 'duration', 'qualification', 'user_type', 'organization', 'requirement', 'classes',
        )