from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .serializers import MessageSerializer
from .models import Message
from .tasks import is_sended

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView


class MessageAPI(viewsets.ViewSet):
    
    def list(self, request, pk=None):
        if pk:
            queryset = Message.objects.filter(id=pk)
        else:
            queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        Message.objects.update(
            is_read=True
        )
        return Response(serializer.data)
        
    
    def create_message(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = Message.objects.create(
                header=serializer.data['header'],
                body=serializer.data['body']
            )
            is_sended.delay(message.id)
            
            return Response({'Message created successfull': 'ok'}, status=200)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        Message.objects.filter(id=pk).delete()
        
        return Response('ok', status=status.HTTP_410_GONE)
        
        
