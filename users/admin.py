from django.contrib import admin
from online_shop.admin import BaseAdmin
from .models import UsersReview, City, Province, ProvinceCities, Address, UserAddress


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


@admin.register(City)
class AdminCity(BaseAdmin):
    list_display = (
        'id',
        'name',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'name',)
    list_filter = ('is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by primary key
    ordering = ('pk',)

    search_fields = ('id', 'name')


@admin.register(Province)
class AdminProvince(BaseAdmin):
    list_display = (
        'id',
        'province_name',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'province_name',)
    list_filter = ('is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by primary key
    ordering = ('pk',)

    search_fields = ('id', 'province_name')


@admin.register(ProvinceCities)
class AdminProvinceCities(BaseAdmin):
    list_display = (
        'id',
        'province',
        'city',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'province',)
    list_filter = ('province', 'is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by primary key
    ordering = ('pk',)

    search_fields = ('id', 'province__province_name', 'city__name')


@admin.register(Address)
class AdminAddress(BaseAdmin):
    list_display = (
        'id',
        'province',
        'city',
        'street',
        'address_details',
        'number',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'province',)
    list_filter = ('province', 'is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by primary key
    ordering = ('pk',)

    search_fields = ('id', 'province__province_name', 'city__name')


@admin.register(UserAddress)
class AdminUserAddress(BaseAdmin):
    list_display = (
        'id',
        'user',
        'address',
        'is_default',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'user',)
    list_filter = ('user', 'is_default', 'is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by primary key
    ordering = ('pk',)

    search_fields = ('id', 'user__id', 'user__name')
