# Generated by Django 2.1 on 2018-08-21 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': '选项', 'verbose_name_plural': '选项'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '问题', 'verbose_name_plural': '问题'},
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发布日期'),
        ),
    ]
