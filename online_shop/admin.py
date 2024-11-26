from django.contrib import admin
from .models import Category, Insurance, Product, PurchaseBasket


# My actions
@admin.action(description='Activate all selected items')
def activate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Deactivate all selected items')
def deactivate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=False)


class BaseAdmin(admin.ModelAdmin):

    # Actions
    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )


@admin.register(Category)
class AdminCategory(BaseAdmin):
    list_display = (
        'id',
        'title',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'title',)
    list_filter = ('is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by primary key
    ordering = ('pk',)

    search_fields = ('title',)


@admin.register(Insurance)
class AdminInsurance(BaseAdmin):
    list_display = (
        'id',
        'name',
        'insurance_type',
        'expires',
        'description',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'name',)
    list_filter = ('is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by primary key
    ordering = ('pk',)

    search_fields = ('id', 'name', 'insurance_type', 'description',)


@admin.register(Product)
class AdminProduct(BaseAdmin):
    list_display = (
        'id',
        'title',
        'price',
        'category',
        'insurance',
        'image',
        'description',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'title',)
    list_filter = ('price', 'category', 'is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by primary key
    ordering = ('pk',)

    search_fields = (
        'id', 'title', 'category__title', 'insurance__name'
    )


@admin.register(PurchaseBasket)
class AdminPurchaseBasket(BaseAdmin):
    list_display = (
        'id',
        'user',
        'product',
        'count',
        'total_price',
        'is_completed',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'user', 'product',)
    list_filter = ('user', 'is_completed', 'is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by primary key
    ordering = ('pk',)

    search_fields = ('id', 'user__username', 'product__title',)
