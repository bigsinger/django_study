# Generated by Django 2.1 on 2018-08-23 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0015_auto_20180823_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ram',
            name='manufacturer_id',
        ),
    ]
