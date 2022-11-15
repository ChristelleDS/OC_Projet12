from django.contrib import admin
from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_created', 'status')


admin.site.register(Contract, ContractAdmin)
