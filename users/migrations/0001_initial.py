# Generated by Django 4.2 on 2024-11-29 16:35

from django.db import migrations, models
import django.db.models.deletion
import online_shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('online_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date and time')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date and time')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('rate', models.IntegerField(default=0, validators=[online_shop.models.validate_rate], verbose_name='Rate')),
                ('description', models.TextField(verbose_name='Description')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_shop.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'UserReview',
                'verbose_name_plural': 'UserReviews',
            },
        ),
    ]
