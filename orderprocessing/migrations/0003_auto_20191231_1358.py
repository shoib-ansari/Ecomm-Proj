# Generated by Django 2.2.2 on 2019-12-31 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderprocessing', '0002_checkout_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='payment_option',
            field=models.CharField(default=None, max_length=60, null=True),
        ),
    ]