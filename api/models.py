from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    header = models.CharField(max_length=50, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Тело сообщения')
    is_sended = models.BooleanField(default=False, verbose_name='Сообщение отправлено', blank=True)
    is_read = models.BooleanField(default=False, verbose_name='Сообщение прочитано', blank=True)
    
    def __str__(self):
        return self.header
    
    def __repr__(self):
        return self.header
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'