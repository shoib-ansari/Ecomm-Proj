# Generated by Django 2.2.2 on 2020-03-20 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_group_products_categort'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group_products',
            old_name='categort',
            new_name='category',
        ),
    ]
