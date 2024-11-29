# Generated by Django 4.2 on 2024-11-29 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date and time')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date and time')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date and time')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date and time')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('insurance_type', models.CharField(verbose_name='Insurance type')),
                ('expires', models.CharField(verbose_name='Expiration after delivery')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Insurance',
                'verbose_name_plural': 'Insurances',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date and time')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date and time')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('price', models.FloatField(verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_shop.category', verbose_name='Category')),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_shop.insurance', verbose_name='Insurance')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='PurchaseBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date and time')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date and time')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('count', models.IntegerField(default=1, verbose_name='Count')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Is completed')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_shop.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'PurchaseBasket',
                'verbose_name_plural': 'PurchaseBaskets',
            },
        ),
        migrations.CreateModel(
            name='ProductPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date and time')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date and time')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_shop.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'ProductPicture',
                'verbose_name_plural': 'ProductPictures',
            },
        ),
    ]
