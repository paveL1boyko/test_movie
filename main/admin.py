from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.functional import lazy
from django.utils.translation import gettext, gettext_lazy as _

from .models import AdvUser

gettext_lazy = lazy(gettext, str)


@admin.register(AdvUser)
class AdvNewUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'send_message'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
