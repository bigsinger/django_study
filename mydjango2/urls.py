"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from mysite import views as mysite_view
from login import views as login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', mysite_view.index, name='index'),            # 首页
    url(r'^index/$', login_view.login_log, name='index'),   # 首页
    url(r'^blog/', include('blog.urls')),                   # 博客
    url(r'^vote/', include('vote.urls')),                   # 投票
    url(r'^assets/', include('assets.urls')),
]