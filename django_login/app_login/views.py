from django.shortcuts import render, redirect
from django.http import HttpResponse

# 指定函数识别到登陆信息才能执行
from django.contrib.auth.decorators import login_required

# 实现登陆功能
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        # 如果已经成功登陆，直接在首页显示登录名
        return render(request, 'app_login/index.html', context={'username': request.user.username})
    else:
        # 如果没有登陆，以匿名展示
        return render(request, 'app_login/index.html', context={'username': False})


def user_login(request):
    if request.method == "GET":
        return render(request, 'app_login/login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 去数据库中校验
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 登陆并把信息写入session
            login(request, user)
            # 跳转到首页
            return redirect('/shop/', )
        else:
            # 用户名和密码验证不正确
            return render(request, 'app_login/login.html', context={'error': '用户名或密码错误！'})


def user_logout(request):
    # 注销，清楚session
    logout(request)

    # 返回到登陆页面
    return redirect('/shop/login/')


def interface(request):

    return render(request, 'app_login/interface.html', context={'username': request.user.username})
