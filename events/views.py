from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .models import Event, Status
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
        """
        Only a contributor of the project can get the list of issues.
        :return: list of issues for the project in param
        """
        contract = get_object_or_404(Client, pk=self.kwargs['contract_pk'])
        self.check_object_permissions(self.request, contract)
        return Event.objects.filter(contract_id=self.kwargs['contract_pk'])

    def perform_create(self, serializer):
        """
        Add actions to execute during the saving of the instance:
        - save the request.user as the author and default assignee
        """
        contract = get_object_or_404(Contract, pk=self.kwargs['contract_pk'])
        self.check_object_permissions(self.request, contract)
        event = serializer.save(client=self.kwargs['client_pk'],
                                contract=self.kwargs['contract_id'])

    def retrieve(self, request, contract_pk=None, pk=None, *args, **kwargs):
        """
        Check requested data:
        - if project and issue don't match: error "unknown data" is raised
        - if match : return detailed data if permissions ok
        """
        contract = get_object_or_404(Contract, pk=contract_pk)
        event = get_object_or_404(Event, pk=pk)
        if event.contract.id == contract.id:
            self.check_object_permissions(self.request, event)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        else:
            return Response('Unknown data requested', status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, contract_pk=None, pk=None, *args, **kwargs):
        contract = get_object_or_404(Contract, contract_pk=contract_pk)
        event = get_object_or_404(Event, pk=pk)
        if event.contract.id == contract.id:
            self.check_object_permissions(self.request, event)
            serializer = EventSerializer(contract, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Unknown data requested', status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)
        self.check_object_permissions(self.request, event)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
