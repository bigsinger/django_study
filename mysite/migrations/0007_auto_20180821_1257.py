# Generated by Django 2.1 on 2018-08-21 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20180820_1923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterModelOptions(
            name='userlevel',
            options={'verbose_name': '用户等级', 'verbose_name_plural': '用户等级'},
        ),
    ]
