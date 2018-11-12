from django.shortcuts import render, redirect
from django.http import HttpResponse

# 引入定义的所有类--- table(. 表示当前文件夹）
from . import models


# Create your views here.
def save_data(request):
    """
    读取文件数据，并写入数据库
    :param request:
    :return:
    """
    path = r'student/static/students.txt'

    # 存储读取过程中的错误
    msg = ''

    # 开始读取
    try:
        with open(path, mode='r', encoding='utf-8-sig') as f:
            current_line = f.readline()
            print(current_line)
            while current_line:
                student_info = current_line.strip().replace('\n', '').split(',')
                obj_student = models.Student(sno=student_info[0],
                                             name=student_info[1],
                                             gender=student_info[2],
                                             birthday=student_info[3],
                                             mobile=student_info[4],
                                             email=student_info[5],
                                             address=student_info[6])
                # 保存
                obj_student.save()

                # 读取下一行
                current_line = f.readline()
    except Exception as e:
        msg = e
        print(msg)

    return HttpResponse('录入成功！' + msg)


def index(request):
    sno = request.GET.get('sno')
    if sno is None:
        # 获取所有的学生信息
        students = models.Student.objects.all()
        return render(request, 'index.html', context={'students': students})
    else:
        # 获取一条信息
        stu = models.Student.objects.get(pk=sno)
        return render(request, 'stu_detail.html', context={'student': stu})


def stu_add(request):
    if request.method == "GET":
        return render(request, 'stu_add.html')
    elif request.method == "POST":
        sno = request.POST.get('sno')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')

        obj_student = models.Student(sno=sno,
                                     name=name,
                                     gender=gender,
                                     birthday=birthday,
                                     mobile=mobile,
                                     email=email,
                                     address=address)
        # 保存
        obj_student.save()

        return redirect('/student/index/')


def stu_detail(request, sno):
    stu = models.Student.objects.get(pk=sno)
    return render(request, 'stu_detail.html', context={'student': stu})


def stu_modify(request, sno):
    if request.method == "GET":
        stu = models.Student.objects.get(pk=sno)
        return render(request, 'stu_modify.html', context={'student': stu})

    elif request.method == "POST":

        sno = request.POST.get('sno')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')

        student = models.Student.objects.get(pk=sno)
        student.name = name
        student.gender = gender
        student.birthday = birthday
        student.mobile = mobile
        student.email = email
        student.address = address
        student.save()
        return redirect('/student/index/')


def stu_delete(request, sno):
    stu = models.Student.objects.get(pk=sno)
    stu.delete()
    return redirect('/student/index/')
