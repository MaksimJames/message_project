from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .serializers import MessageSerializer
from .models import Message
from .tasks import is_sended
from .throttles import PostRateThrottle

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema


class MessageAPI(viewsets.ViewSet):
    throttle_scope = 'post'
    
    def list(self, request, pk=None):
        '''
            Get list of all message
        '''
        if pk:
            queryset = Message.objects.filter(id=pk)
        else:
            queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        Message.objects.update(
            is_read=True
        )
        return Response(serializer.data)
    
    @swagger_auto_schema(query_serializer=MessageSerializer)
    def create_message(self, request):
        '''
            Create message
        '''
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
        '''
            For delete message by pk
        '''
        Message.objects.filter(id=pk).delete()
        
        return Response('ok', status=status.HTTP_410_GONE)
    
    def read_unread_message(self, request):
        '''
            For read unread message only, not all
        '''
        queryset = Message.objects.filter(is_read=False)
        if queryset:
            serializer = MessageSerializer(queryset, many=True)
            Message.objects.update(is_read=True)
            return Response(serializer.data)
        else:
            return Response('All message was read', status=status.HTTP_404_NOT_FOUND)
        
        
