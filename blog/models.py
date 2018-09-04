# coding: utf-8

from django.db import models
from django.conf import settings

# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField(max_length=10, verbose_name='标签名')

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.CASCADE)
    date_time = models.DateField(auto_now_add=True, verbose_name='发布日期')
    content = models.TextField(blank=True, null=True, verbose_name='内容')
    digest = models.TextField(blank=True, null=True, verbose_name='摘要')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
    view = models.BigIntegerField(default=0, verbose_name='浏览数')
    comment = models.BigIntegerField(default=0, verbose_name='评论数')
    picture = models.CharField(max_length=200, verbose_name='标题图片地址')
    tag = models.ManyToManyField(Tag, '标签')

    def __str__(self):
        return self.title

    def sourceUrl(self):
        source_url = settings.HOST + '/blog/detail/{id}'.format(id=self.pk)
        return source_url  # 给网易云跟帖使用

    def viewed(self):
        """
        增加阅读数
        :return:
        """
        self.view += 1
        self.save(update_fields=['view'])

    def commenced(self):
        """
        增加评论数
        :return:
        """
        self.comment += 1
        self.save(update_fields=['comment'])

    class Meta:  # 按时间降序
        ordering = ['-date_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='类别')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    last_mod_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')

    class Meta:
        ordering = ['name']
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    source_id = models.CharField(max_length=25, verbose_name='文章id或source名称')
    create_time = models.DateTimeField(auto_now=True, verbose_name='评论时间')
    user_name = models.CharField(max_length=25, verbose_name='评论用户')
    url = models.CharField(max_length=100, verbose_name='链接')
    comment = models.CharField(max_length=500, verbose_name='评论内容')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name