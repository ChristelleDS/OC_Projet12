from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'company', 'qualification', 'salescontact')
    list_filter = ('company', 'qualification', 'salescontact')


admin.site.register(Client, ClientAdmin)
