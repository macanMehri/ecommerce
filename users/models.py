from django.db import models
import online_shop.models as om
from django.contrib.auth.models import User


class City(om.BaseModel):
    name = models.CharField(max_length=255, blank=False, verbose_name='Name')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.name}'


class Province(om.BaseModel):
    province_name = models.CharField(max_length=255, blank=False, verbose_name='Province name')

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'

    def __str__(self):
        return f'{self.province_name}'


class ProvinceCities(om.BaseModel):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name='Province')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='City')

    class Meta:
        verbose_name = 'ProvinceCity'
        verbose_name_plural = 'ProvinceCities'

    def __str__(self):
        return f'{self.province} - {self.city}'


class Address(om.BaseModel):
    title = models.CharField(max_length=255, blank=False, verbose_name='Title')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name='Province')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='City')
    street = models.CharField(max_length=255, blank=False, verbose_name='Street')
    address_details = models.TextField(blank=False, verbose_name='Address details')
    number = models.CharField(max_length=255, blank=False, verbose_name='Number')

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.street} - {self.number}'


class UserAddress(om.BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Address')
    is_default = models.BooleanField(default=False, verbose_name='Is default')

    class Meta:
        verbose_name = 'UserAddress'
        verbose_name_plural = 'UserAddresses'

    def __str__(self):
        return f'{self.address}'


class UsersReview(om.BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(om.Product, on_delete=models.CASCADE, verbose_name='Product')
    rate = models.IntegerField(default=0, verbose_name='Rate', validators=[om.validate_rate])
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name = 'UserReview'
        verbose_name_plural = 'UserReviews'

    def __str__(self):
        return f'{self.rate}'
