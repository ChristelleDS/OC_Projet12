from django.db import models
from django.contrib.auth import get_user_model
from clients.models import Client


User = get_user_model()


class Contract(models.Model):
    id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Client, related_name='contracts',
                               on_delete=models.CASCADE, blank=False)
    salescontact = models.ForeignKey(User, related_name='contracts',
                                     on_delete=models.SET_NULL, null=True,
                                     limit_choices_to={"team": 'SALES'})
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False) # signé ou non
    amount = models.FloatField(default=0)
    payment_due = models.DateTimeField(blank=True)

    def __str__(self):
        return str(self.client) + " (contract: " + str(self.id) + " )"
