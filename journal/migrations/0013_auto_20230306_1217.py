# Generated by Django 3.2.18 on 2023-03-06 12:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0012_auto_20230306_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='date',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='time',
        ),
        migrations.AddField(
            model_name='trade',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
