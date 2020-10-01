from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_per_page = 10
    search_fields = ('name', 'email', 'phone')


admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)
