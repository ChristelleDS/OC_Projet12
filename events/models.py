from django.db import models
from clients.models import Client
from contracts.models import Contract
from authentication.models import User


class Status(models.Model):
    id = models.BigAutoField(primary_key=True)
    status_label = models.CharField(max_length=18)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __str__(self):
        return self.status_label


class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.OneToOneField(to=Contract, related_name='events',
                                    on_delete=models.CASCADE, null=True)  # limit_choices_to={"status": True}
    client = models.ForeignKey(Client, related_name='events',
                               on_delete=models.CASCADE, blank=True)
    supportcontact = models.ForeignKey(User, related_name='events',
                                       on_delete=models.SET_NULL, null=True,
                                       limit_choices_to={"team": 'SUPPORT'})
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_status = models.ForeignKey(Status, related_name='events',
                                     on_delete=models.SET_NULL, null=True)
    attendees = models.IntegerField(default=1)
    event_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.client) + " (event: " + str(self.id) + " )"
