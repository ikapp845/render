# Generated by Django 4.0.3 on 2023-01-28 09:46

import datetime
from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_profile_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=user.models.upload_to),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 28, 15, 16, 0, 537367), null=True),
        ),
    ]
