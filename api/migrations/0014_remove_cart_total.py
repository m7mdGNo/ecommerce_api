# Generated by Django 4.1.1 on 2022-09-26 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_item_remove_cart_products_remove_cart_total_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
    ]
