from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    # Add custom fields to be displayed in the admin
    list_display = ['email', 'username', 'first_name', 'last_name', 'phone_number', 'weight', 'height', 'body_part', 'sex', 'is_staff', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'weight', 'height', 'body_part', 'sex')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'weight', 'height', 'body_part', 'sex')}),
    )

admin.site.register(User, CustomUserAdmin)