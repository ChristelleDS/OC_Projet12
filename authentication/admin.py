from django.contrib import admin
from .models import User
from django import forms
from django.forms import PasswordInput, ModelForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin

"""
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password',
                  'first_name', 'last_name',
                  'last_login', 'date_joined',
                  'is_active', 'team')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
"""

class CustomUserAdmin(UserAdmin):
    # form = UserChangeForm
    # add_form = CustomUserForm
    username = None
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
    readonly_fields = ('last_login', 'date_joined',)
    exclude = ("username",)
    # self.exclude.append('username')

admin.site.register(User, CustomUserAdmin)


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
