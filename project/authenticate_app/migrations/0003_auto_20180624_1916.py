# Generated by Django 2.0.6 on 2018-06-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate_app', '0002_auto_20180624_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='subject',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]