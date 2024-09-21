from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from core.signals import user_signal
from celery import shared_task
import time
# Create your models here.


class common(models.Model):
    is_active = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserInfo(common):
    name = models.CharField(max_length=150)

# @receiver(post_save, sender=UserInfo)
@receiver(user_signal)
def show(sender, instance, created, **kwargs):
    # Call the Celery task asynchronously
    process_long_running_task.delay(sender, instance, created)

@shared_task
def process_long_running_task(sender, instance, created):
    time.sleep(10)  # Simulate a long-running task
    print(sender)
    print(instance)
    print(created)