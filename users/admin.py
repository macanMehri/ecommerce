from django.contrib import admin
from online_shop.admin import BaseAdmin
from .models import UsersReview


@admin.register(UsersReview)
class AdminUsersReview(BaseAdmin):
    list_display = (
        'id',
        'user',
        'product',
        'rate',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'user', 'product',)
    list_filter = ('rate', 'product__category', 'is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by primary key
    ordering = ('pk',)

    search_fields = (
        'id', 'product__name', 'rate',
    )
