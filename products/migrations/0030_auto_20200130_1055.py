# Generated by Django 2.2.2 on 2020-01-30 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_auto_20200130_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group_products',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product_group',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='product_group',
            name='heading',
        ),
        migrations.AddField(
            model_name='group_products',
            name='Image',
            field=models.ImageField(blank=True, upload_to='HomePage_Categories'),
        ),
        migrations.AddField(
            model_name='group_products',
            name='heading',
            field=models.CharField(default='Try out', max_length=400),
        ),
        migrations.AddField(
            model_name='product_group',
            name='product',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
    ]
