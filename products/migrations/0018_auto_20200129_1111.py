# Generated by Django 2.2.2 on 2020-01-29 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20200129_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_group',
            name='products',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Product_Group',
        ),
    ]
