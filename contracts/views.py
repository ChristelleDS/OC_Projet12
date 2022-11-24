from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Contract
from clients.models import Client
from .serializers import ContractListSerializer, ContractSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .permissions import ContractPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filter import ContractFilter


User = get_user_model()


class ContractViewset(ModelViewSet):
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated & ContractPermission]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = ContractFilter
    search_fields = ["client__lastname", "salescontact", "status"]

    def get_queryset(self):
        client = get_object_or_404(Client, pk=self.kwargs['client_pk'])
        self.check_object_permissions(self.request, client)
        return Contract.objects.filter(client_id=self.kwargs['client_pk'])

    def perform_create(self, serializer):
        client = get_object_or_404(Client, pk=self.kwargs['client_pk'])
        self.check_object_permissions(self.request, client)
        contract = serializer.save(client=client,
                                   salescontact=self.request.user)

    def retrieve(self, request, client_pk=None, pk=None, *args, **kwargs):
        contract = get_object_or_404(Contract, pk=pk)
        client = get_object_or_404(Client, pk=client_pk)
        if contract.client.id == client.id:
            self.check_object_permissions(self.request, contract)
            serializer = ContractSerializer(contract)
            return Response(serializer.data)
        else:
            return Response('Unknown data requested', status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, client_pk=None, pk=None, *args, **kwargs):
        contract = get_object_or_404(Contract, pk=pk)
        client = get_object_or_404(Client, pk=client_pk)
        if contract.client.id == client.id:
            self.check_object_permissions(self.request, contract)
            serializer = ContractSerializer(contract, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Unknown data requested', status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, client_pk=None, pk=None, *args, **kwargs):
        contract = get_object_or_404(Contract, pk=pk)
        self.check_object_permissions(self.request, contract)
        contract.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
