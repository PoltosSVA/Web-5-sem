# Generated by Django 4.2.5 on 2023-11-19 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmcatalog', '0013_alter_countdown_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='nov', max_length=15)),
                ('discount', models.DecimalField(decimal_places=1, max_digits=3)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='countdown',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 19, 23, 54, 59, 356182)),
        ),
    ]
