from django.contrib import admin
from .models import Dolgozok, Alapanyag, Megrendelesek,CustomUser
#Anyagtipus
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'raktaros', 'lezervago')

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Additional info', {
            'fields': ('raktaros', 'lezervago')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Additional info', {
            'fields': ('raktaros', 'lezervago')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
   

admin.site.register(Dolgozok)
admin.site.register(Alapanyag)
admin.site.register(Megrendelesek)
admin.site.register(CustomUser, CustomUserAdmin)
