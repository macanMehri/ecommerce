from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


def category_view(request):
    categories = Category.objects.filter(is_active=True)

    return render(request, 'categories.html', {'categories': categories})


def product_view(request, category_id):
    products = Product.objects.filter(is_active=True, category__id=category_id)

    return render(request, 'products.html', {'products': products})


@login_required
def add_product_view(request):

    if request.user.is_staff:

        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.is_active = True
                product.save()
                return redirect('categories')

        else:
            form = ProductForm()

        return render(request, 'add_product.html', {'form': form})

    print("You do not have permission to delete this menu item.")
    return redirect('categories')


