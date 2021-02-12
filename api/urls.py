
from django.contrib import admin
from django.urls import path

from .views import MessageAPI

urlpatterns = [
    path('api', MessageAPI.as_view({
        'get': 'list',
        'post': 'create_message',
    })),
    path('api/<int:pk>/', MessageAPI.as_view({
        'get': 'list',
        'delete': 'destroy'
    })),
    path('api/unread', MessageAPI.as_view({
        'get': 'read_unread_message'
    }))
]
