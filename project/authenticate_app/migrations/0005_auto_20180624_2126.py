# Generated by Django 2.0.6 on 2018-06-24 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate_app', '0004_auto_20180624_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='date_field',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
