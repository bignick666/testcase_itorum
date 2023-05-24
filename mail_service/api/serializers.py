from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from entities.models import Entity, Client, Message


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'phone_number', 'code', 'tag')


class EntitySerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField(many=True)

    class Meta:
        model = Entity
        fields = ('id', 'start_date', 'text', 'client', 'end_date')


class MessageSerializer(serializers.ModelSerializer):
    entity = serializers.StringRelatedField(many=False, read_only=True)
    client = serializers.StringRelatedField(many=True)

    class Meta:
        model = Message
        fields = ('id', 'date', 'entity', 'client')
