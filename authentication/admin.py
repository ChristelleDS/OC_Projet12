from django.contrib import admin
from .models import User
from django.contrib.admin.models import LogEntry


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
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

# admin.site.register(User, CustomUserAdmin)


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = 'action_time'

    # to filter the resultes by users, content types and action flags
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'action_flag',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser
