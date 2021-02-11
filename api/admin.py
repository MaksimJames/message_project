from django.contrib import admin

from .models import Message


#admin.site.register(Message)
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fields = ('header', 'body', 'is_sended', 'is_read')
