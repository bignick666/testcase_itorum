from rest_framework import viewsets, permissions

from .serializers import (EntitySerializer,
                          ClientSerializer,
                          MessageSerializer)
from entities.models import Client, Entity, Message


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
