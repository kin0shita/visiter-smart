from django.contrib import admin
# CustomUserをインポート
from .models import Reception0, Reception1, Reception3, CustomUser


class Reception0Admin(admin.ModelAdmin):
    model = Reception0
    list_display = ('id', 'user', 'purpose', 'accompany', 'companion_last_name', 'companion_first_name', 'relationship2', 'visited_at')
    list_display_links = ('id', 'user', 'purpose', 'accompany', 'companion_last_name', 'companion_first_name', 'relationship2')
    list_filter = (
        'id',
        'user',
        'purpose',
        'accompany'
        )
    

    search_fields = ('id', 'accompany', 'companion_last_name', 'companion_first_name')
    ordering = ('id', 'accompany', 'companion_last_name', 'companion_first_name')

class Reception1Admin(admin.ModelAdmin):
    model = Reception1
    list_display = ('user', 'bt1', 'bt2', 'InHospital')
    list_display_links = ('user', 'InHospital')
    list_filter = (
        'user',
        'InHospital',
        )
    
    search_fields = ('id', 'InHospital')
    ordering = ('id', 'InHospital')

class Reception3Admin(admin.ModelAdmin):
    model = Reception3
    list_display = ('OutHospital', 'active')
    list_display_links = ('OutHospital', 'active')
    list_filter = (
        
        'OutHospital',
        'active'
        )
    search_fields = ('id', 'OutHospital', 'active')
    ordering = ('id', 'OutHospital', 'active')

admin.site.register(Reception0, Reception0Admin)
admin.site.register(Reception1, Reception1Admin)
admin.site.register(Reception3, Reception3Admin)
