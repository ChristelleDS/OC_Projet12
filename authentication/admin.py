from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'team')
    search_fields = ('email', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups',)
    fieldsets = (
        (None, {'fields': ('email', 'password',
                           'first_name', 'last_name',
                           'last_login', 'date_joined',
                           'is_active', 'team')}),
    )

admin.site.register(User, UserAdmin)
