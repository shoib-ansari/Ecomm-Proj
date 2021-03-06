# Generated by Django 2.2.2 on 2020-01-28 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200127_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalcategory',
            name='add_to_main_header',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='finalcategory',
            name='add_to_sub_header',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='finalcategory',
            name='image',
            field=models.ImageField(default='hello', upload_to='Category_images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maincategory',
            name='add_to_main_header',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='maincategory',
            name='add_to_sub_header',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='maincategory',
            name='image',
            field=models.ImageField(default='hello', upload_to='Category_images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='add_to_main_header',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='add_to_sub_header',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(default='hello', upload_to='Category_images'),
            preserve_default=False,
        ),
    ]
