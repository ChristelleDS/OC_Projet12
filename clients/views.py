from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filter import ClientFilter
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer, ClientListSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .permissions import ClientPermission


User = get_user_model()


class ClientViewset(ModelViewSet):
    permission_classes = [ClientPermission]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = ClientFilter
    search_fields = ["firstname", "lastname", "email", "company", "qualification"]

    def get_queryset(self):
        return Client.objects.all()

    def perform_create(self, serializer):
        client = serializer.save()

    def retrieve(self, request, pk=None, *args, **kwargs):
        client = get_object_or_404(Client, pk=pk)
        print(client)
        self.check_object_permissions(self.request, client)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        client = get_object_or_404(Client, pk=pk)
        self.check_object_permissions(self.request, client)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        client = get_object_or_404(Client, pk=pk)
        self.check_object_permissions(self.request, client)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
