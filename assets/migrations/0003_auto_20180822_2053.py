# Generated by Django 2.1 on 2018-08-22 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20180822_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='asset',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assets.Asset', verbose_name='关联资产'),
        ),
    ]
