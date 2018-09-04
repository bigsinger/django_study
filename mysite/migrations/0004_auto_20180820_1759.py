# Generated by Django 2.1 on 2018-08-20 09:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20180820_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200, verbose_name='选项')),
                ('votes', models.IntegerField(default=0, verbose_name='选择数')),
            ],
        ),
        migrations.CreateModel(
            name='UserLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=5, verbose_name='用户级别')),
                ('desc', models.CharField(max_length=20, verbose_name='级别说明')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布日期'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Question'),
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='mysite.UserLevel'),
            preserve_default=False,
        ),
    ]
