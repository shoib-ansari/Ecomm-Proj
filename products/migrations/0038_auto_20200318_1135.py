# Generated by Django 2.2.2 on 2020-03-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_remove_group_products_catregory_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
