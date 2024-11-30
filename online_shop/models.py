from django.db import models
from django.contrib.auth.models import User
import users.models as um


def validate_rate(value):
    if value < 0 or value > 5:
        raise ValidationError('Product rate must be between numbers 0 and 5!')


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created date and time')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated date and time')
    is_active = models.BooleanField(default=False, verbose_name='Is active')

    class Meta:
        abstract = True

    def __str__(self):
        raise NotImplementedError('Please override the method!')


class Category(BaseModel):
    title = models.CharField(max_length=255, blank=False, verbose_name='Title')
    image = models.ImageField(verbose_name='Image')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.title}'


class Insurance(BaseModel):
    name = models.CharField(max_length=255, blank=False, verbose_name='Name')
    insurance_type = models.CharField(blank=False, verbose_name='Insurance type')
    # For how long the insurance lasts
    expires = models.CharField(blank=False, verbose_name='Expiration after delivery')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name = 'Insurance'
        verbose_name_plural = 'Insurances'

    def __str__(self):
        return f'{self.name} - {self.insurance_type}'


class Product(BaseModel):
    title = models.CharField(max_length=255, blank=False, verbose_name='Title')

    price = models.FloatField(verbose_name='Price')

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Category'
    )

    insurance = models.ForeignKey(
        Insurance, on_delete=models.CASCADE, verbose_name='Insurance'
    )

    description = models.TextField(blank=False, verbose_name='Description')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    @property
    def rate(self):
        reviews = um.UsersReview.objects.filter(is_active=True)
        total = 0
        for review in reviews:
            total += review.rate

        count = len(reviews)
        if count > 0:
            average = total / count
        else:
            average = 0

        return average

    def __str__(self):
        return f'{self.title}'


class ProductPicture(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    image = models.ImageField(verbose_name='Image')

    class Meta:
        verbose_name = 'ProductPicture'
        verbose_name_plural = 'ProductPictures'

    def __str__(self):
        return f'{self.product.title}'


class PurchaseBasket(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    count = models.IntegerField(default=1, verbose_name='Count')
    is_completed = models.BooleanField(default=False, verbose_name='Is completed')

    class Meta:
        verbose_name = 'PurchaseBasket'
        verbose_name_plural = 'PurchaseBaskets'

    def __str__(self):
        return f'{self.product}'

    @property
    def total_price(self):
        return self.product.price * self.count
