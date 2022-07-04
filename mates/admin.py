from django.contrib import admin
from .models import CustomUser
from .forms import RegisterUserForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = RegisterUserForm

    fieldsets=(
        *UserAdmin.fieldsets,(
            'User miscallenous',
            {
                'fields':(
                    'accept_terms',
                    'gender',
                )
            }
        )    )
admin.site.register(CustomUser,CustomUserAdmin)