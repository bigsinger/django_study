import datetime
from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=300, verbose_name='问题')
    # pub_date = models.DateTimeField(default=timezone.now, verbose_name='发布日期')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='发布日期')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = verbose_name


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='选项')
    votes = models.IntegerField(default=0, verbose_name='选择数')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = '选项'
        verbose_name_plural = verbose_name
