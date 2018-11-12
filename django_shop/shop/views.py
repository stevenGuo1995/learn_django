from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
import random
# 登陆之后才能访问
from django.contrib.auth.decorators import login_required

# 身份认证，登陆，注销
from django.contrib.auth import authenticate, login, logout
# 获取用户组信息
from django.contrib.auth.models import Group
from . import models


# Create your views here.
class Customer:
    def __init__(self):
        self.produce_list = [models.SalesListDetail(product_id='6005004003001',
                                                    product_name='康师傅牛肉面', product_price=40.0, product_unit='箱',
                                                    product_num=1,
                                                    total_money=40.0),
                             models.SalesListDetail(product_id='6005004003006',
                                                    product_name='雪花啤酒', product_price=60.5, product_unit='箱',
                                                    product_num=1,
                                                    total_money=65.5)]
        self.serial_num = ''
        self.get_serial_num()
        self.total_num = 0
        self.total_price = 0

    # 生成流水单号
    def get_serial_num(self):
        now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        s = random.randint(0, 9999)
        self.serial_num = str(now_time) + '{:04d}'.format(int(s))

    # 计算商品总量及总价格
    def get_total(self):
        self.total_num = 0
        self.total_price = 0

        for product in self.produce_list:
            self.total_num += product.product_num
            self.total_price += product.total_money


current_buy = Customer()


def user_login(request):
    if request.method == "GET":
        # 加载登陆界面，让用户登陆
        return render(request, 'shop/login.html')
    elif request.method == "POST":
        # 提交登陆请求

        # 获取填写的用户名，密码
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 进行身份验证，把结果赋给user变量
        user = authenticate(request, username=username, password=password)

        # 根据user结果来判断
        if user is not None:
            # 用户名跟密码验证成功

            # 登陆并且保存当前用户session
            login(request, user)

            # 获取用户组
            current_group = str(Group.objects.get(user=user))

            # 根据用户所属组返回相应页面
            if current_group == 'cashierGroup':
                return redirect('/shop/cashier/')

            elif current_group == 'adminGroup':
                return redirect('/shop/admin')

            elif current_group == 'storageGroup':
                return redirect('/shop/storage')

        else:
            return render(request, 'shop/login.html', context={'error': '用户名或密码错误'})


def user_logout(request):
    logout(request)
    return redirect('/shop/login/')


@login_required
def user_cashier(request):
    # 统计数量和金额
    current_buy.get_total()
    return render(request, 'shop/cashier.html',
                  context={'username': request.user.username, 'current_buy': current_buy})


@login_required
def user_admin(request):
    return render(request, 'shop/admin.html', context={'username': request.user.username})


@login_required
def user_storage(request):
    return render(request, 'shop/storage.html', context={'username': request.user.username})


@login_required
def product_add(request):
    product_id = request.GET.get('product_id')
    for product in current_buy.produce_list:
        if product.product_id == product_id:
            product.product_num += 1
            product.total_money = product.product_num * product.product_price
            return redirect('/shop/cashier/')
    obj_product = models.Product.objects.get(pk=product_id)
    one_product = models.SalesListDetail(product_id=obj_product.product_id,
                                         product_name=obj_product.product_name,
                                         product_price=obj_product.product_price,
                                         product_unit=obj_product.product_unit,
                                         product_num=1,
                                         total_money=obj_product.product_price)
    current_buy.produce_list.append(one_product)
    print(current_buy.produce_list)
    return redirect('/shop/cashier/')


@login_required
def product_del(request):
    product_id = request.GET.get('product_id')
    for index, product in enumerate(current_buy.produce_list):
        if product.product_id == product_id:
            current_buy.produce_list.pop(index)
    return redirect('/shop/cashier/')


@login_required
def commit(request):
    # 在SalesList中插入销售记录
    obj_sales_list = models.SalesList(
        serial_num=current_buy.serial_num,
        total_num=current_buy.total_num,
        total_money=current_buy.total_price,
        receive_money=1,
        return_money=1,
        user_cashier=request.user.username
    )


def init_customer():
    current_buy.produce_list.clear()
    current_buy.serial_num = ""
    current_buy.total_num = 0
    current_buy.total_money = 0.0
    current_buy.receive_money = 0.0
    current_buy.return_money = 0.0
    # 生成一个新的单号
    current_buy.get_serial_num()
