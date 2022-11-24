from rest_framework.serializers import ModelSerializer
from .models import Client
from django.contrib.auth import get_user_model


User = get_user_model()


class ClientListSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'firstname', 'lastname', 'company', 'qualification', 'salescontact']


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
