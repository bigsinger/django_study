# coding: utf-8

from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class UserLevel(models.Model):
    '''
    用户分类
    '''
    level = models.IntegerField(default=5, verbose_name='用户级别')
    desc = models.CharField(max_length=20, verbose_name='级别说明')

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name = '用户等级'
        verbose_name_plural = verbose_name


class User(models.Model):
    username = models.CharField(max_length=30, verbose_name='用户名')
    level = models.ForeignKey('UserLevel', on_delete=models.CASCADE)
    userpass = models.CharField(max_length=30, verbose_name='密码')
    useremail = models.EmailField(max_length=30, verbose_name='邮箱')
    adddate = models.DateTimeField(default=timezone.now, verbose_name='添加日期', editable=False)
    # oprator = models.CharField(max_length=30, verbose_name='操作人')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
