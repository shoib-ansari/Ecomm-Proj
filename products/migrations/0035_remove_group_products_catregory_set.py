# Generated by Django 2.2.2 on 2020-03-17 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_auto_20200317_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group_products',
            name='catregory_set',
        ),
    ]
