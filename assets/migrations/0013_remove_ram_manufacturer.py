# Generated by Django 2.1 on 2018-08-23 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0012_ram_manufacturer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ram',
            name='manufacturer',
        ),
    ]
