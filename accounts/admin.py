from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'email_verified', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Email Verification', {'fields': ('email_verified', 'verification_token')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Email Verification', {'fields': ('email_verified',)}),
    )
