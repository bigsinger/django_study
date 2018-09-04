from django.shortcuts import render
from login import models  # 导入models文件

# Create your views here.


def login_log(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username + ' ' + password)

        # 将数据保存到数据库
        models.UserInfo.objects.create(user=username, pswd=password)

    # 从数据库中读取所有数据，注意缩进
    user_list = models.UserInfo.objects.all()
    return render(request, 'login/index.html', {'data': user_list})