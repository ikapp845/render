# Generated by Django 4.0.3 on 2023-01-10 15:06

from django.db import migrations, models
import group.models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.CharField(default=group.models.key_generator, editable=False, max_length=6, primary_key=True, serialize=False, unique=True),
        ),
    ]
