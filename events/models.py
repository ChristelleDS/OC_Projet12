from django.db import models
from clients.models import Client
from contracts.models import Contract
from django.contrib.auth import get_user_model


User = get_user_model()


class Status(models.Model):
    id = models.BigAutoField(primary_key=True)
    status_label = models.CharField(max_length=18)

    def __str__(self):
        return self.status_label


class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.ForeignKey(Contract, related_name='events',
                                 on_delete=models.CASCADE, blank=False)
    client = models.ForeignKey(Client, related_name='events',
                               on_delete=models.CASCADE, blank=False)
    supportcontact = models.ForeignKey(User, related_name='events',
                                       on_delete=models.SET_NULL, null=True,
                                       limit_choices_to={"team": 'SUPPORT'})
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_status = models.ForeignKey(Status, related_name='events',
                                     on_delete=models.SET_NULL, null=True)
    attendees = models.IntegerField(default=1)
    event_date = models.DateTimeField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.client) + " (event: " + str(self.id) + " )"
