# Generated by Django 2.2.2 on 2020-01-17 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_reviewimages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='Review',
            new_name='review',
        ),
    ]
