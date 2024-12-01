from django.shortcuts import render, redirect
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
def add_address_view(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.save()
            user_address, _ = UserAddress.objects.get_or_create(
                user=request.user,
                address=address,
                defaults={'is_default': False},
            )
            # return redirect('')

    else:
        form = AddressForm()

    return render(request, 'add_address.html', {'form': form})

