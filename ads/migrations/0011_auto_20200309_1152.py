# Generated by Django 3.0.3 on 2020-03-09 11:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0010_auto_20200309_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='adlist',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='adlist',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 9, 11, 52, 11, 996104, tzinfo=utc)),
        ),
    ]
