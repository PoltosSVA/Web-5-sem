# Generated by Django 4.2.5 on 2023-11-18 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmcatalog', '0004_alter_countdown_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countdown',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 18, 22, 5, 28, 756920)),
        ),
    ]
