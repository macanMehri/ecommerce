from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Address
from django.core.validators import EmailValidator


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['title', 'province', 'city', 'street', 'address_details', 'number']


class ChangeUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'New Username',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter new username'}),
        }


class ChangeEmailForm(forms.Form):
    new_email = forms.EmailField(
        label="New Email",
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Enter your new email"}),
        validators=[EmailValidator()],
    )
    confirm_email = forms.EmailField(
        label="Confirm Email",
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Confirm your new email"}),
        validators=[EmailValidator()],
    )

    def clean(self):
        cleaned_data = super().clean()
        new_email = cleaned_data.get("new_email")
        confirm_email = cleaned_data.get("confirm_email")

        if new_email and confirm_email and new_email != confirm_email:
            raise forms.ValidationError("Emails do not match. Please try again.")

        return cleaned_data
