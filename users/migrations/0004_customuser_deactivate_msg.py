# Generated by Django 3.0.3 on 2020-03-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200304_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='deactivate_msg',
            field=models.CharField(max_length=300, null=True),
        ),
    ]