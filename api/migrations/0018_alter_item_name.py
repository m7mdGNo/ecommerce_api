# Generated by Django 4.1.1 on 2022-09-26 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_rename_number_item_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product'),
        ),
    ]
