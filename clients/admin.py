from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'company_name', 'qualification')


admin.site.register(Client, ClientAdmin)
