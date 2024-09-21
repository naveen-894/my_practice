from django.urls import path
from .views import UserViewset

urlpatterns = [
    path('create', UserViewset.as_view({'post': 'create'}))
]