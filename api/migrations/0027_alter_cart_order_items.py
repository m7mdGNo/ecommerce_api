# Generated by Django 4.1.1 on 2022-09-29 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order_items',
            field=models.ManyToManyField(null=True, to='api.item'),
        ),
    ]
