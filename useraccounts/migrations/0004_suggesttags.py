# Generated by Django 2.2.2 on 2020-01-08 08:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0003_auto_20200104_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuggestTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.TextField(max_length=4000)),
                ('user', models.ForeignKey(on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
