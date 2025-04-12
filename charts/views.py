from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from online_shop.models import PurchaseBasket
from django.db.models import Q
from online_shop.models import Product


CURRENT_YEAR = datetime.now().year


@login_required
def last_year_total_money(request):
    if request.user.is_superuser:
        purchases = PurchaseBasket.objects.filter(is_completed=True)
        purchases = purchases.filter(
            Q(updated_date__year=CURRENT_YEAR)
        )
        each_month_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for purchase in purchases:
            each_month_purchases[purchase.updated_month-1] += purchase.total_price
        return render(request, 'total_purchase_chart.html',
                      {'each_month_purchases': each_month_purchases})
    else:
        return redirect('index')


@login_required
def last_year_total_amount(request):
    if request.user.is_superuser:
        purchases = PurchaseBasket.objects.filter(is_completed=True)
        purchases = purchases.filter(
            Q(updated_date__year=CURRENT_YEAR)
        )
        each_month_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for purchase in purchases:
            each_month_purchases[purchase.updated_month-1] += purchase.count
        return render(request, 'total_amount_chart.html',
                      {'each_month_purchases': each_month_purchases})
    else:
        return redirect('index')


@login_required
def last_year_total_purchase_of_product(request, product_id):
    if request.user.is_superuser:
        product = get_object_or_404(Product, id=product_id)
        purchases = PurchaseBasket.objects.filter(is_completed=True, product=product)
        purchases = purchases.filter(
            Q(updated_date__year=CURRENT_YEAR)
        )
        each_month_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for purchase in purchases:
            each_month_purchases[purchase.updated_month-1] += purchase.count
        return render(request, 'total_purchase_of_product.html',
                      {'each_month_purchases': each_month_purchases, 'product': product})
    else:
        return redirect('index')

