from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ['header', 'body']
        
