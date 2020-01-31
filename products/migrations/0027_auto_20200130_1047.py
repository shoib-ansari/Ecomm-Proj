# Generated by Django 2.2.2 on 2020-01-30 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20200130_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_group',
            name='product',
        ),
        migrations.CreateModel(
            name='Group_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
