# Generated by Django 4.0.3 on 2023-01-11 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0010_alter_groupquestion_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupquestion',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 22, 21, 50, 214208), null=True),
        ),
    ]
