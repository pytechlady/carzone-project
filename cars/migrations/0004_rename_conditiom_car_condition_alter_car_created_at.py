# Generated by Django 4.0.2 on 2022-02-11 23:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_created_at_alter_car_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='conditiom',
            new_name='condition',
        ),
        migrations.AlterField(
            model_name='car',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 11, 23, 4, 15, 985140)),
        ),
    ]
