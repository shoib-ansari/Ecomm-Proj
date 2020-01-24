# Generated by Django 2.2.2 on 2020-01-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='products.Tags'),
        ),
    ]
