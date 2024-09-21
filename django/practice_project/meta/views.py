from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import UserInfo
from core.signals import user_signal
# from django.dispatch import Signal, receiver


class UserViewset(ModelViewSet):

    def create(self, request):
        # Create the UserInfo instance
        instance = UserInfo.objects.create(name="naveen")

        # Trigger the signal manually
        user_signal.send(sender=UserInfo, instance=instance, created='khk')
        return Response('created_successfully')