from django.contrib import admin
from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_created', 'status', 'salescontact')
    list_filter = ('client', 'status', 'salescontact')


admin.site.register(Contract, ContractAdmin)
