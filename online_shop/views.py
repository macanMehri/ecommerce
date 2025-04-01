from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Insurance, PurchaseBasket, ProductPicture, Discount
from .forms import (
    ProductForm, CategoryForm, InsuranceForm, UsersReviewForm, ProductPictureForm, DiscountForm
)
import users.models as um
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F, Q


def index_view(request):
    categories = Category.objects.filter(is_active=True)[:6]
    return render(request, 'index.html', {'categories': categories})


def all_products(request):
    query = request.GET.get('query', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    category_id = request.GET.get('category')
    discount_filter = request.GET.get('discount')

    # Fetch active products
    products = Product.objects.filter(is_active=True).order_by('-popularity')

    # Apply search query
    if query:
        products = products.filter(
            Q(title__icontains=query) | Q(category__title__icontains=query)
        )

    # Apply raw price filter (instead of `price` property)
    if min_price and min_price.isdigit():
        products = products.filter(raw_price__gte=float(min_price))
    if max_price and max_price.isdigit():
        products = products.filter(raw_price__lte=float(max_price))

    # Apply category filter
    if category_id and category_id.isdigit():
        products = products.filter(category_id=int(category_id))

    # Apply discount filter
    if discount_filter:  # Checking for discount presence
        products = products.exclude(discount__isnull=True).exclude(discount__percentage=0)

    # Fetch all categories for the filter
    categories = Category.objects.filter(is_active=True)

    return render(request, 'all_products.html', {
        'products': products,
        'query': query,
        'categories': categories,
        'request': request,
    })


@login_required
def control_panel(request):
    if request.user.is_staff:
        return render(request, 'control_panel.html')


def calculate_total(purchases) -> float:
    total = 0
    for purchase in purchases:
        total += purchase.total_price
    return total


def category_view(request):
    categories = Category.objects.filter(is_active=True).order_by('title')

    return render(request, 'categories.html', {'categories': categories})


def product_view(request, category_id):
    products = Product.objects.filter(is_active=True, category__id=category_id).order_by('-popularity')
    category = get_object_or_404(Category, id=category_id)

    return render(request, 'products.html', {'products': products, 'category': category})


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
            form = CategoryForm(request.POST, request.FILES)
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
        redirect('index')


@login_required
def add_offer_view(request):
    if request.user.is_staff:

        if request.method == 'POST':
            form = DiscountForm(request.POST)
            if form.is_valid():
                offer = form.save(commit=False)
                offer.is_active = True
                offer.save()
                return redirect('offers')
        else:
            form = DiscountForm()

        return render(request, 'add_offer.html', {'form': form})
    else:
        redirect('index')


@login_required
def offers_view(request):
    if request.user.is_staff:
        offers = Discount.objects.filter(is_active=True).order_by('title')
        return render(request, 'offers.html', {'offers': offers})
    else:
        redirect('index')


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
def delete_offer_view(request, offer_id):
    if request.user.is_staff:
        offer = get_object_or_404(Discount, id=offer_id)

        if request.method == 'POST':
            offer.delete()
            return redirect('offers')

        return render(
            request, 'confirm_offer_delete.html', {'offer': offer}
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
    if not request.user.is_staff:
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
    if not request.user.is_staff:
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

    product.popularity = F('popularity') + 1
    product.save()

    images = ProductPicture.objects.filter(product=product, is_active=True)

    reviews = um.UsersReview.objects.filter(product=product, is_active=True)

    return render(
        request, 'a_product.html', {
            'product': product, 'images': images, 'reviews': reviews, 'number_of_reviews': len(reviews)
        }
    )


@login_required
def add_to_basket(request, product_id):
    if not request.user.is_staff:
        product = get_object_or_404(Product, id=product_id)

        product.popularity = F('popularity') + 2
        product.save()

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


@login_required
def add_review_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = UsersReviewForm(request.POST, product)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('a_product', product_id=product_id)
    else:
        form = UsersReviewForm()

    return render(request, 'add_review.html', {'form': form, 'product': product})


@login_required
def add_product_picture_view(request, product_id):
    if request.user.is_staff:
        product = get_object_or_404(Product, id=product_id)
        if request.method == 'POST':
            form = ProductPictureForm(request.POST, request.FILES)
            if form.is_valid():
                product_picture = form.save(commit=False)
                product_picture.product = product
                product_picture.is_active = True
                product_picture.save()
                return redirect('a_product', product_id=product.id)
        else:
            form = ProductPictureForm()
        return render(
            request, 'add_product_picture.html', {'form': form, 'product': product}
        )


@login_required
def delete_product_picture_view(request, product_picture_id):
    if request.user.is_staff:
        product_picture = get_object_or_404(ProductPicture, id=product_picture_id)

        if request.method == 'POST':
            product_picture.delete()
            return redirect('a_product', product_id=product_picture.product.id)

        return render(
            request, 'confirm_product_picture_delete.html', {'product_picture': product_picture}
        )


@login_required
def edit_product_view(request, product_id):
    if request.user.is_staff:
        product = get_object_or_404(Product, id=product_id)

        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('a_product', product_id=product.id)
        else:
            form = ProductForm(instance=product)

        return render(request, 'edit_product.html', {'form': form})


@login_required
def edit_offer_view(request, offer_id):
    if request.user.is_staff:
        offer = get_object_or_404(Discount, id=offer_id)

        if request.method == 'POST':
            form = DiscountForm(request.POST, instance=offer)
            if form.is_valid():
                form.save()
                return redirect('offers')
        else:
            form = DiscountForm(instance=offer)

        return render(request, 'edit_offer.html', {'form': form})


@login_required
def edit_category_view(request, category_id):
    if request.user.is_staff:
        category = get_object_or_404(Category, id=category_id)

        if request.method == 'POST':
            form = CategoryForm(request.POST, request.FILES, instance=category)
            if form.is_valid():
                form.save()
                return redirect('categories')
        else:
            form = CategoryForm(instance=category)

        return render(request, 'edit_category.html', {'form': form})


@login_required
def edit_insurance_view(request, insurance_id):
    if request.user.is_staff:
        insurance = get_object_or_404(Insurance, id=insurance_id)

        if request.method == 'POST':
            form = InsuranceForm(request.POST, instance=insurance)
            if form.is_valid():
                form.save()
                return redirect('insurances')
        else:
            form = InsuranceForm(instance=insurance)

        return render(request, 'edit_insurance.html', {'form': form})
