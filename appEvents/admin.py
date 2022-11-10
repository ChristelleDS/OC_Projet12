from django.contrib import admin
from .models import Client, Contract, Status, Event


admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Status)
admin.site.register(Event)
