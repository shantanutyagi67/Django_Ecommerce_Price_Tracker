# Generated by Django 3.1.5 on 2021-01-27 21:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210128_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 27, 21, 50, 10, 367473, tzinfo=utc)),
        ),
    ]
