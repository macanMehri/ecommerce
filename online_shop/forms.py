from django import forms
from .models import Product, Category, Insurance


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'category', 'insurance', 'description']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ['name', 'insurance_type', 'expires', 'description']
