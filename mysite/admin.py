from django.contrib import admin
from .models import User
from .models import UserLevel

# Register your models here.


class UserDisplay(admin.ModelAdmin):
    list_display = ('username', 'level', 'useremail', 'adddate')  # 自定义显示字段


class UserLevelDisplay(admin.ModelAdmin):
    list_display = ('level', 'desc')  # 自定义显示字段


admin.site.register(User, UserDisplay)
admin.site.register(UserLevel, UserLevelDisplay)