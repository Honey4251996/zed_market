# Generated by Django 3.0.3 on 2020-03-09 12:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20200309_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 9, 12, 42, 57, 288864, tzinfo=utc)),
        ),
    ]
