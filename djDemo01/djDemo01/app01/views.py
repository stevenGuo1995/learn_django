from django.http import HttpResponse
from django.shortcuts import render
from app01.externalfun import operfile
import pymysql
# from djDemo01.settings import *

DB_HOST = '192.168.182.10'
DB_USER = 'root'
DB_PASSWORD = '1234.Com'
DB_NAME = 'LibraryDB'

# Create your views here.

def index(request):
    return HttpResponse("Hello,world!")

def login(request):
    return render(request,'login.html')

def course(request):
    return render(request, 'index.html')

def student(request):

    # 1. 准备数据
    path = r"D:\doc\student01.txt"
    students = operfile.read_from_file_dict_by_readline(path)
    # 2. 用获得的数据填充HTML
    return render(request, 'student.html', context={"data":students})


def testdb(request):

    # 连接数据库
    conn = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    # 创建一个操作数据库的指针
    cursor = conn.cursor()

    if request.method == "GET":

        # 获取数据库的数据
        # 准备SQL语句
        sql = "select BookId,BookName,BookTypeId,BookAuthor,BookPressID,BookPrice,BookSumNo " \
            "from Book "

    elif request.method == "POST":

        bookid = request.POST.get('bookid')
        # 连接数据库获取当前bookid的值
        sql = "select BookId,BookName,BookTypeId,BookAuthor,BookPressID,BookPrice,BookSumNo " \
              "from Book Where BookId = '%s'" % (bookid)
    # 展示数据
    cursor.execute(sql)
    results = cursor.fetchall()
    return render(request, 'book.html', context={"data": results})


def authorall(request):
    # 创建一个和数据库的连接
    conn = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    # 为连接创建一个指针
    cursor = conn.cursor()
    # 准备SQL语句
    sql = "Select AuthorId,AuthorName,AuthorAge,AuthorCity,AuthorTelNO," \
          "AuthorEmail,AuthorWorkAddress from Author "
    print(sql)
    # 执行查询
    cursor.execute(sql)
    # 获取结果
    results = cursor.fetchall()
    # 展示页面
    return render(request, 'author.html', context={"authors": results})

def author(request,authorid):

    # 创建一个和数据库的连接
    conn = pymysql.connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME)
    # 为连接创建一个指针
    cursor = conn.cursor()
    # 准备SQL语句
    sql= "Select AuthorId,AuthorName,AuthorAge,AuthorCity,AuthorTelNO," \
         "AuthorEmail,AuthorWorkAddress from Author where AuthorId = '%s'" % authorid
    print(sql)
    # 执行查询
    cursor.execute(sql)
    # 获取结果
    results = cursor.fetchall()
    # 展示页面
    return render(request, 'author.html',context={"authors":results})

def press(request,pressid):
    # 创建一个数据库连接
    # 创建一个和数据库的连接
    conn = pymysql.connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME)
    # 为连接创建一个指针
    cursor = conn.cursor()
    # 准备SQL语句
    sql = "Select PressId,PressName,PressCity,PressTelNO,PressEmail,PressAddress " \
          "from Press where PressId ='%s'" %(pressid)

    print(sql)
    # 执行查询
    cursor.execute(sql)
    # 获取结果
    result = cursor.fetchone()
    # 展示页面
    return render(request,'press.html', context={"press":result})




def test(request,bookid,bookname):
    text="图书编号：" + bookid  +"\n"
    text += "图名名称：" + bookname
    return HttpResponse(text)