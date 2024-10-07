from rest_framework import viewsets
from .models import login,Event
from  .serializer import EventSerializer,LoginSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset=login.objects.all()
    serializer_class=LoginSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer