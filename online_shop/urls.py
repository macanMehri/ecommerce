from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import (
    category_view, product_view, add_product_view, add_category_view, insurances_view,
    add_insurance_view, purchase_basket_view, a_product_view, add_to_basket, increment_purchase,
    decrement_purchase, purchase_history_view
)


urlpatterns = [
    path('categories/', category_view, name='categories'),
    path('products/<int:category_id>', product_view, name='products'),
    path('insurances/', insurances_view, name='insurances'),
    path('logout/', LogoutView.as_view(next_page='/online_shop/categories/'), name='logout'),
    path('add_product/', add_product_view, name='add_product'),
    path('add_category/', add_category_view, name='add_category'),
    path('add_insurance/', add_insurance_view, name='add_insurance'),
    path('purchase_basket/', purchase_basket_view, name='purchase_basket'),
    path('purchase_history/', purchase_history_view, name='purchase_history'),
    path('a_product/<int:product_id>/', a_product_view, name='a_product'),
    path('add_to_basket/<int:product_id>/', add_to_basket, name='add_to_basket'),
    path('increment_purchase/<int:purchase_id>/', increment_purchase, name='increment_purchase'),
    path('decrement_purchase/<int:purchase_id>/', decrement_purchase, name='decrement_purchase'),
]
