# Generated by Django 2.2.2 on 2020-01-04 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='alt_contact',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='postal_add',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.BigIntegerField(null=True),
        ),
    ]
