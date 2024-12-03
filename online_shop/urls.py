from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import (
    category_view, product_view, add_product_view, add_category_view, insurances_view,
    add_insurance_view, purchase_basket_view, a_product_view, add_to_basket, increment_purchase,
    decrement_purchase, purchase_history_view, delete_category_view, delete_insurance_view,
    delete_product_view, add_review_view, add_product_picture_view, delete_product_picture_view,
    edit_category_view, edit_insurance_view, edit_product_view, all_products, control_panel
)


urlpatterns = [
    path('control_panel/', control_panel, name='control_panel'),
    path('all_products/', all_products, name='all_products'),
    path('categories/', category_view, name='categories'),
    path('products/<int:category_id>', product_view, name='products'),
    path('insurances/', insurances_view, name='insurances'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('add_product/', add_product_view, name='add_product'),
    path('add_category/', add_category_view, name='add_category'),
    path('add_insurance/', add_insurance_view, name='add_insurance'),
    path('purchase_basket/', purchase_basket_view, name='purchase_basket'),
    path('purchase_history/', purchase_history_view, name='purchase_history'),
    path('a_product/<int:product_id>/', a_product_view, name='a_product'),
    path('add_to_basket/<int:product_id>/', add_to_basket, name='add_to_basket'),
    path('increment_purchase/<int:purchase_id>/', increment_purchase, name='increment_purchase'),
    path('decrement_purchase/<int:purchase_id>/', decrement_purchase, name='decrement_purchase'),
    path('confirm_category_delete/<int:category_id>', delete_category_view, name='confirm_category_delete'),
    path('confirm_insurance_delete/<int:insurance_id>', delete_insurance_view, name='confirm_insurance_delete'),
    path(
        'confirm_product_picture_delete/<int:product_picture_id>',
        delete_product_picture_view,
        name='confirm_product_picture_delete'
    ),
    path('confirm_product_delete/<int:product_id>', delete_product_view, name='confirm_product_delete'),
    path('add_review/<int:product_id>/', add_review_view, name='add_review'),
    path('add_product_picture/<int:product_id>/', add_product_picture_view, name='add_product_picture'),
    path('edit_product/<int:product_id>/', edit_product_view, name='edit_product'),
    path('edit_category/<int:category_id>/', edit_category_view, name='edit_category'),
    path('edit_insurance/<int:insurance_id>/', edit_insurance_view, name='edit_insurance'),
]
