# Generated by Django 2.1 on 2018-08-21 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20180821_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(auto_now_add=True, verbose_name='发布日期'),
        ),
    ]
