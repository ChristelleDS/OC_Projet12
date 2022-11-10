from django.contrib import admin
from .models import Client, Contract, Status, Event


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'company_name', 'qualification')


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_created', 'status')


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'event_date', 'event_status')


admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
# admin.site.register(Status)
admin.site.register(Event, EventAdmin)
