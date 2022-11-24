from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Event
from django.contrib.auth import get_user_model


User = get_user_model()


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'contract', 'client', 'supportcontact', 'event_date', 'event_status']


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

    def validate_supportcontact(self, value):
        contact = get_object_or_404(User, pk=value.id)
        if contact.team != 'SUPPORT':
            raise ValidationError("This user is not a support member")
        return value
