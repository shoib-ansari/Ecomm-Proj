# Generated by Django 2.2.2 on 2020-01-25 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200122_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Keywords',
        ),
    ]