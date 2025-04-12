from django.urls import path
from .views import last_year_total_money, last_year_total_amount, last_year_total_purchase_of_product


urlpatterns = [
    path('total_purchase/', last_year_total_money, name='total_purchase'),
    path('total_amount/', last_year_total_amount, name='total_amount'),
    path('total_purchase_product/<int:product_id>', last_year_total_purchase_of_product, name='total_purchase_product'),
]