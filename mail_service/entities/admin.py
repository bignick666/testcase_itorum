from django.contrib import admin

from .models import Entity, Client, Message


class ClientAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'tag')
    list_filter = ('code', 'tag')


class EntityAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date')
    list_filter = ('client', 'start_date', 'end_date')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('date', 'entity', 'client')


admin.site.register(Entity, EntityAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Message, MessageAdmin)

