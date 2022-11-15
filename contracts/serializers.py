from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Contract
from django.contrib.auth import get_user_model


User = get_user_model()


class ContractListSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id', 'client', 'salescontact', 'status']


class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'
