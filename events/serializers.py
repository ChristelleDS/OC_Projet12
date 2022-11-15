from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Event
from django.contrib.auth import get_user_model


User = get_user_model()


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'contract', 'client', 'supportcontact', 'event_status']


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
