# Generated by Django 2.2.2 on 2020-01-06 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderprocessing', '0004_auto_20200106_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='status',
        ),
        migrations.AddField(
            model_name='ordered_products',
            name='status',
            field=models.IntegerField(choices=[(1, 'Placed by user'), (2, 'seen'), (3, 'delivered'), (4, 'approved by User'), (5, 'In Return request')], default=1),
        ),
    ]
