# Generated by Django 2.2.2 on 2020-01-29 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200129_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_group',
            name='products',
        ),
        migrations.CreateModel(
            name='Category_Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='category_group',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='products.Category_Products'),
            preserve_default=False,
        ),
    ]
