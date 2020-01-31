# Generated by Django 2.2.2 on 2020-01-29 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20200129_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_group',
            name='product',
        ),
        migrations.AddField(
            model_name='product_group',
            name='product',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
