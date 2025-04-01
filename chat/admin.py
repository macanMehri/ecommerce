from django.contrib import admin
from online_shop.admin import *
from .models import Message, Connection


@admin.register(Message)
class AdminMessage(BaseAdmin):
    list_display = (
        'id',
        'sender_user',
        'responder_user',
        'sent_text',
        'respond_text',
        'is_responded',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id',)
    list_filter = ('is_responded', 'is_active', 'created_date', 'updated_date', 'sender_user', 'responder_user')
    list_editable = ('is_active', 'is_responded')
    # Order by primary key
    ordering = ('-created_date',)

    search_fields = ('sender_user', 'responder_user')


@admin.register(Connection)
class AdminConnection(BaseAdmin):
    list_display = (
        'id',
        'user',
        'admin',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id',)
    list_filter = ('user', 'admin', 'is_active', 'created_date', 'updated_date',)
    list_editable = ('is_active',)
    # Order by primary key
    ordering = ('-created_date',)

    search_fields = ('user', 'admin')
