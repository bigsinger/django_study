# Generated by Django 2.1 on 2018-08-23 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0016_remove_ram_manufacturer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ram',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Manufacturer', verbose_name='制造商'),
        ),
    ]
