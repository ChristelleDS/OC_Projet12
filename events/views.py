from django.core.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .models import Event
from clients.models import Client
from contracts.models import Contract
from .serializers import EventListSerializer, EventSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .permissions import EventPermission


User = get_user_model()


class EventViewset(ModelViewSet):
    serializer_class = EventListSerializer
    detail_serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated & EventPermission]

    def get_queryset(self):
        contract = get_object_or_404(Contract, pk=self.kwargs['contract_pk'])
        self.check_object_permissions(self.request, contract)
        return Event.objects.filter(contract_id=self.kwargs['contract_pk'])

    def perform_create(self, serializer):
        contract = get_object_or_404(Contract, pk=self.kwargs['contract_pk'])
        if Event.objects.filter(contract=contract.id).exists():
            raise ValidationError("This contract already have an associated event.")
        if contract.status is False:
            raise ValidationError("This contract is not signed yet.")
        self.check_object_permissions(self.request, contract)
        client = get_object_or_404(Client, pk=contract.client.id)
        event = serializer.save(client=client, contract=contract)

    def retrieve(self, request, contract_pk=None, pk=None,
                 *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)
        contract = get_object_or_404(Contract, pk=contract_pk)
        if event.contract.id == contract.id:
            self.check_object_permissions(self.request, event)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        else:
            return Response('Unknown data requested',
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, contract_pk=None, pk=None,
               *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)
        contract = get_object_or_404(Contract, pk=contract_pk)
        if event.contract.id == contract.id:
            self.check_object_permissions(self.request, event)
            serializer = EventSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Unknown data requested',
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)
        self.check_object_permissions(self.request, event)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
