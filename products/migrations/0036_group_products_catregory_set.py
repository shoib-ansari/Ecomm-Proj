# Generated by Django 2.2.2 on 2020-03-17 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_remove_group_products_catregory_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_products',
            name='catregory_set',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Category_set'),
            preserve_default=False,
        ),
    ]
