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
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    qualification = models.fields.CharField(max_length=10,
                                            choices=QUALIFICATION,
                                            default='PROSPECT')
    salescontact = models.ForeignKey(User, related_name='clients',
                                     on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.company_name + " ( " + str(self.id) + " )"
