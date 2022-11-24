from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django import forms
from django.contrib.admin.models import LogEntry
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



class registerUserForm(UserCreationForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'team')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    add_form = registerUserForm
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
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'team', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('last_login', 'date_joined',)
    exclude = ("username",)


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
