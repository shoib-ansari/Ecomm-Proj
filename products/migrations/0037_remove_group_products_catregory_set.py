# Generated by Django 2.2.2 on 2020-03-17 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_group_products_catregory_set'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group_products',
            name='catregory_set',
        ),
    ]
