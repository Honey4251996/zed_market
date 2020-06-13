# Generated by Django 3.0.3 on 2020-03-25 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_data_value'),
        ('posts', '0003_auto_20200325_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category'),
        ),
    ]
