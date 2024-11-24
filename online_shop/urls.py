from django.urls import path, include
from .views import category_view, product_view


urlpatterns = [
    path('categories/', category_view, name='categories'),
    path('products/<int:category_id>', product_view, name='products'),
]
