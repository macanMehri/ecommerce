from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import (
    category_view, product_view, add_product_view, add_category_view, insurances_view,
    add_insurance_view
)


urlpatterns = [
    path('categories/', category_view, name='categories'),
    path('products/<int:category_id>', product_view, name='products'),
    path('insurances/', insurances_view, name='insurances'),
    path('logout/', LogoutView.as_view(next_page='/online_shop/categories/'), name='logout'),
    path('add_product/', add_product_view, name='add_product'),
    path('add_category/', add_category_view, name='add_category'),
    path('add_insurance/', add_insurance_view, name='add_insurance'),
]
