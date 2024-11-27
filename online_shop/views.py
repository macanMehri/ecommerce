from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Insurance, PurchaseBasket
from .forms import ProductForm, CategoryForm, InsuranceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F


def index_view(request):
    return render(request, 'index.html')


def calculate_total(purchases) -> float:
    total = 0
    for purchase in purchases:
        total += purchase.total_price
    return total


def category_view(request):
    categories = Category.objects.filter(is_active=True).order_by('title')

    return render(request, 'categories.html', {'categories': categories})


def product_view(request, category_id):
    products = Product.objects.filter(is_active=True, category__id=category_id).order_by('-created_date')

    return render(request, 'products.html', {'products': products})


@login_required
def insurances_view(request):
    if request.user.is_staff:
        insurances = Insurance.objects.filter(is_active=True).order_by('name')
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
def delete_category_view(request, category_id):
    if request.user.is_staff:
        category = get_object_or_404(Category, id=category_id)

        if request.method == 'POST':
            category.delete()
            return redirect('categories')

        return render(
            request, 'confirm_category_delete.html', {'category': category}
        )


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
def delete_insurance_view(request, insurance_id):
    if request.user.is_staff:
        insurance = get_object_or_404(Insurance, id=insurance_id)
        if request.method == 'POST':
            insurance.delete()
            return redirect('insurances')

        return render(
            request, 'confirm_insurance_delete.html', {'insurance': insurance}
        )


@login_required
def delete_product_view(request, product_id):
    if request.user.is_staff:
        product = get_object_or_404(Product, id=product_id)

        if request.method == 'POST':
            product.delete()
            return redirect('products', category_id=product.category.id)

        return render(
            request, 'confirm_product_delete.html', {'product': product}
        )


@login_required
def purchase_basket_view(request):
    purchases_to_do = PurchaseBasket.objects.filter(
        user=request.user, is_completed=False,
    ).order_by('-created_date')

    total = calculate_total(purchases=purchases_to_do)

    return render(
        request, 'purchase_basket.html', {
            'purchases_to_do': purchases_to_do, 'total': total
        }
    )


@login_required
def purchase_history_view(request):
    purchases_history = PurchaseBasket.objects.filter(
        user=request.user, is_completed=True
    ).order_by('created_date')

    total = calculate_total(purchases=purchases_history)

    return render(
        request, 'purchase_history.html', {
            'purchases_history': purchases_history, 'total': total
        }
    )


def a_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'a_product.html', {'product': product})


@login_required
def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    basket_item, created = PurchaseBasket.objects.get_or_create(
            user=request.user,
            product=product,
            is_completed=False
    )

    if not created:
        basket_item.count = F('count') + 1
        basket_item.save()

    return redirect('a_product', product_id=product.id)


def increment_purchase(request, purchase_id):
    basket_item = get_object_or_404(PurchaseBasket, id=purchase_id, user=request.user)
    basket_item.count = F('count') + 1
    basket_item.save()
    return redirect('purchase_basket')


def decrement_purchase(request, purchase_id):
    basket_item = get_object_or_404(PurchaseBasket, id=purchase_id, user=request.user)
    if basket_item.count > 1:
        basket_item.count = F('count') - 1
        basket_item.save()
    else:
        basket_item.delete()
    return redirect('purchase_basket')
