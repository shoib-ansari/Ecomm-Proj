# Generated by Django 2.2.2 on 2020-01-29 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_category_group_product_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_group',
            name='group',
        ),
        migrations.AddField(
            model_name='product_group',
            name='group',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='products.Category_Group'),
            preserve_default=False,
        ),
    ]
