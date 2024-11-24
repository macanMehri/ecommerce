from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category


def category_view(request):
    categories = Category.objects.filter(is_active=True)

    return render(request, 'categories.html', {'categories': categories})


def product_view(request, category_id):
    products = Product.objects.filter(is_active=True, category__id=category_id)

    return render(request, 'products.html', {'products': products})

