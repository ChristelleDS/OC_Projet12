from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Client(models.Model):

    QUALIFICATION = [('PROSPECT', 'PROSPECT'), ('CLIENT', 'CLIENT')]

    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=250, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    qualification = models.fields.CharField(max_length=10,
                                            choices=QUALIFICATION,
                                            default='PROSPECT')
    salescontact = models.ForeignKey(User, related_name='clients',
                                     on_delete=models.SET_NULL, null=True)


class Contract(models.Model):
    id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Client, related_name='contracts',
                               on_delete=models.CASCADE, blank=False)
    salescontact = models.ForeignKey(User, related_name='contracts',
                                     on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    payment_due = models.DateTimeField(blank=True)


class Status(models.Model):
    id = models.BigAutoField(primary_key=True)
    status_label = models.CharField(max_length=18)


class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.ForeignKey(Contract, related_name='events',
                                 on_delete=models.CASCADE, blank=False)
    client = models.ForeignKey(Client, related_name='events',
                               on_delete=models.CASCADE, blank=False)
    supportcontact = models.ForeignKey(User, related_name='events',
                                       on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_status = models.ForeignKey(Status, related_name='events',
                                     on_delete=models.SET_NULL, null=True)
    attendees = models.IntegerField(default=1)
    event_date = models.DateTimeField(blank=True)
    notes = models.TextField()
