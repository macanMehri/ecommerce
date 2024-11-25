from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Insurance, PurchaseBasket
from .forms import ProductForm, CategoryForm, InsuranceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def category_view(request):
    categories = Category.objects.filter(is_active=True)

    return render(request, 'categories.html', {'categories': categories})


def product_view(request, category_id):
    products = Product.objects.filter(is_active=True, category__id=category_id)

    return render(request, 'products.html', {'products': products})


@login_required
def insurances_view(request):
    if request.user.is_staff:
        insurances = Insurance.objects.filter(is_active=True)
        return render(request, 'insurances.html', {'insurances': insurances})
    else:
        redirect('categories')


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


@login_required
def add_category_view(request):
    if request.user.is_staff:

        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                category = form.save(commit=False)
                category.is_active = True
                category.save()
                return redirect('categories')
        else:
            form = CategoryForm()

        return render(request, 'add_category.html', {'form': form})

    return redirect('categories')


@login_required
def add_insurance_view(request):
    if request.user.is_staff:

        if request.method == 'POST':
            form = InsuranceForm(request.POST)
            if form.is_valid():
                insurance = form.save(commit=False)
                insurance.is_active = True
                insurance.save()
                return redirect('insurances')
        else:
            form = InsuranceForm()

        return render(request, 'add_insurance.html', {'form': form})
    else:
        redirect('insurances')


@login_required
def purchase_basket_view(request):
    purchases_to_do = PurchaseBasket.objects.filter(user=request.user, is_completed=False)

    return render(
        request, 'purchase_basket.html', {'purchases_to_do': purchases_to_do}
    )


def a_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'a_product.html', {'product': product})
