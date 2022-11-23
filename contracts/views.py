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


User = get_user_model()


class ContractViewset(ModelViewSet):
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated & ContractPermission]

    def get_queryset(self):
        """
        Only a contributor of the project can get the list of issues.
        :return: list of issues for the project in param
        """
        client = get_object_or_404(Client, pk=self.kwargs['client_pk'])
        self.check_object_permissions(self.request, client)
        return Contract.objects.filter(client_id=self.kwargs['client_pk'])

    def perform_create(self, serializer):
        client = get_object_or_404(Client, pk=self.kwargs['client_pk'])
        self.check_object_permissions(self.request, client)
        contract = serializer.save(client=client,
                                   salescontact=self.request.user)

    def retrieve(self, request, client_pk=None, pk=None, *args, **kwargs):
        """
        Check requested data:
        - if project and issue don't match: error "unknown data" is raised
        - if match : return detailed data if permissions ok
        """
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

"""
    @action(detail=True, methods=['PUT'])
    def sign(self, request, pk):
        # Signer le contrat
        contract = get_object_or_404(Contract, pk=pk)
        self.check_object_permissions(self.request, contract)
        contract.status = True
        contract.save()
        # update the client qualification
        client = get_object_or_404(Client, pk=contract.client.id)
        client.QUALIFICATION = 'CLIENT'
        client.save()
        # return a success response (status_code=200 as default)
        return Response()
"""
