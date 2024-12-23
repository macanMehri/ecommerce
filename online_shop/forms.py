from django import forms
from .models import Product, Category, Insurance, ProductPicture, Offer
import users.models as um


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'raw_price', 'category', 'insurance', 'description', 'offer']


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


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['title', 'percentage', 'description']
