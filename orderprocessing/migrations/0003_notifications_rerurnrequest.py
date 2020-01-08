# Generated by Django 2.2.2 on 2020-01-06 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orderprocessing', '0002_checkout_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='RerurnRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(max_length=90000)),
                ('seen_status', models.BooleanField(default=False)),
                ('approved_for_return', models.BooleanField(default=False)),
                ('return_status', models.BooleanField(default=False)),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderprocessing.Checkout')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('notification', models.TextField(default='Your return request has been approved by us we will contact you soon for return pickup', max_length=10000)),
                ('seen_by_user', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('link', models.CharField(blank=True, max_length=400)),
                ('checkout', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orderprocessing.Checkout')),
                ('return_request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orderprocessing.RerurnRequest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
