# Generated by Django 4.1.5 on 2023-01-29 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0006_alter_like_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 29, 23, 0, 23, 855640), null=True),
        ),
    ]
