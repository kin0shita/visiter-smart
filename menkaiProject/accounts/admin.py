from django.contrib import admin
# CustomUserをインポート
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'email', 'email_2',
        'last_name', 'first_name',
        'birthday', 'postal_code', 'address', 'tel', 'patient_id', 'patient_name', 'relationship1',
        'is_staff', 'is_active',
        )
    list_filter = (
        'email',
        'last_name', 'first_name', 'patient_id', 'patient_name', 'relationship1',
        'is_staff', 'is_active',
        )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'last_name', 'first_name',
        'birthday', 'postal_code', 'address', 'tel', 'patient_id', 'patient_name', 'relationship1',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','last_name', 'first_name', 'patient_id', 'patient_name',)
    ordering = ('email','last_name', 'first_name', 'patient_id', 'patient_name',)


admin.site.register(CustomUser, CustomUserAdmin) 