from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, SignUpForm, AddressForm, ChangeUsernameForm, ChangeEmailForm
from django.contrib.auth import authenticate, login
from online_shop import templates
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProvinceCities, Province, Address, UserAddress
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm


def login_view(request):
    if request.user.is_authenticated:
        messages.error(request, "You are already logged in!")
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
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
            return redirect('/')
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
            return redirect('dashboard')
    else:
        form = AddressForm()

    return render(request, 'add_address.html', {'form': form, 'provinces': provinces})


@login_required
def user_dash_view(request):
    addresses = UserAddress.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'addresses': addresses})


@login_required
def delete_address(request, user_address_id):
    user_address = get_object_or_404(UserAddress, id=user_address_id)

    if request.method == 'POST':
        user_address.delete()
        return redirect('dashboard')

    return render(
        request, 'confirm_address_delete.html', {'user_address': user_address}
    )


@login_required
def change_username(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Username updated successfully!')
            return redirect('dashboard')
    else:
        form = ChangeUsernameForm(instance=request.user)
    return render(request, 'change_username.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important for staying logged in
            messages.success(request, 'Password updated successfully!')
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required
def change_email(request):
    if request.method == "POST":
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data["new_email"]
            request.user.email = new_email
            request.user.save()
            messages.success(request, "Your email has been updated successfully.")
            return redirect("dashboard")
    else:
        form = ChangeEmailForm()

    return render(request, 'change_email.html', {"form": form})
