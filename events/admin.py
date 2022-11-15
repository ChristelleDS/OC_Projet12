from django.contrib import admin
from .models import Status, Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'event_date', 'event_status')

admin.site.register(Status)
admin.site.register(Event, EventAdmin)
