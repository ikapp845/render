# Generated by Django 4.0.3 on 2023-02-01 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0008_alter_like_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 1, 18, 40, 59, 38101), null=True),
        ),
    ]
