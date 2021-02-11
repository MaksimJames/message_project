
from celery import shared_task
from .models import Message
from .celery import app



@shared_task
def is_sended(id):
    Message.objects.filter(id=id).update(is_sended=True)
    