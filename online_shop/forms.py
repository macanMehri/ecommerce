from django import forms
from .models import Product, Category, Insurance, ProductPicture, Discount
import users.models as um


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'raw_price', 'category', 'insurance', 'description', 'discount']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'image']


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ['name', 'insurance_type', 'expires', 'description']


class UsersReviewForm(forms.ModelForm):
    class Meta:
        model = um.UsersReview
        fields = ['rate', 'description']


class ProductPictureForm(forms.ModelForm):
    class Meta:
        model = ProductPicture
        fields = ['image']


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['title', 'percentage', 'description']
