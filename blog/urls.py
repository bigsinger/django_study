# coding: utf-8
from django.conf.urls import url
from . import views as blog_view

app_name = 'blog'


urlpatterns = [
    url(r'^$', blog_view.index, name='index'),            # 首页
    url(r'^about/$', blog_view.about, name='about'),
    url(r'^archive/$', blog_view.archive, name='archive'),
    url(r'^link/$', blog_view.link, name='link'),
    url(r'^comment$', blog_view.comment, name='comment'),
    url(r'^blog/(?P<pk>\d+)/$', blog_view.blog, name='article'),
    url(r'^getcomment/$', blog_view.get_comment, name='getcomment'),
    url(r'^detail/(?P<pk>\d+)/$', blog_view.detail, name='detail'),
    url(r'^detail/(?P<pk>\d+)$', blog_view.detail, name='detail'),
    url(r'^search/$', blog_view.search, name='search'),
    url(r'^tag/(?P<name>.*?)/$', blog_view.tag, name='tag'),
]