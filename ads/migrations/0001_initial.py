# Generated by Django 3.0.3 on 2020-03-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('ad_type', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('item_price', models.FloatField()),
                ('email', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('zip_code', models.CharField(max_length=100, null=True)),
                ('contact_number', models.CharField(max_length=20, null=True)),
                ('premium_options', models.CharField(max_length=100)),
                ('payment_method', models.CharField(max_length=100)),
            ],
        ),
    ]
