from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Client
from epicEvents.contracts.serializers import ContractListSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class ClientListSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'firstname', 'lastname', 'company_name', 'qualification', 'salescontact']


class ClientDetailSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
