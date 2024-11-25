from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'category', 'insurance', 'description']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
