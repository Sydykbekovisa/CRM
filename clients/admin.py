from django.contrib import admin

from .models import Client


admin.site.register(Client)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')
    search_fields = ('name',)
