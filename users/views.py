from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, SignUpForm, AddressForm
from django.contrib.auth import authenticate, login
from online_shop import templates
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProvinceCities, Province, Address, UserAddress
from django.http import JsonResponse


def login_view(request):
    if request.user.is_authenticated:
        messages.error(request, "You are already logged in!")
        return redirect('categories')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('categories')
        else:
            form.add_error(None, 'Invalid username or password! Please try again.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def get_cities(request, province_id):
    cities = ProvinceCities.objects.filter(province_id=province_id).select_related('city')
    city_data = [{'id': city.city.id, 'name': city.city.name} for city in cities]
    return JsonResponse({'cities': city_data})


@login_required
def add_address_view(request):
    provinces = Province.objects.all()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.save()
            UserAddress.objects.get_or_create(
                user=request.user,
                address=address,
                defaults={'is_default': False},
            )
            # return redirect('')
    else:
        form = AddressForm()

    return render(request, 'add_address.html', {'form': form, 'provinces': provinces})


@login_required
def my_addresses_view(request):
    addresses = Address.objects.filter(
        id__in=UserAddress.objects.filter(user=request.user).values_list('address', flat=True))
    return render(request, 'my_addresses.html', {'addresses': addresses})
