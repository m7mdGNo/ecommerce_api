# Generated by Django 4.1.1 on 2022-09-25 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='media/prodcut_imgs'),
        ),
    ]
