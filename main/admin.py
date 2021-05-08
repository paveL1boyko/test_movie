from django.contrib import admin

# from .forms import RegisterUserForm, AdminRegisterUserForm
from .forms import AdminRegisterUserForm
from .models import AdvUser


# Register your models here.

@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    form = AdminRegisterUserForm
    autocomplete_fields = ['groups']
    list_display = ('username', 'email')
    field_order = ('username', 'email')
    search_fields = ['username']
    save_on_top = True

    def get_fields(self, request, obj=None):
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'send_message',
                  'is_active', 'is_staff', 'is_superuser', 'user_permissions',
                  'groups', ('date_joined', 'last_login')]
        if not obj:
            fields = ['username', 'password1', 'password2', 'email']
        return fields
