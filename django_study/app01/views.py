from django.http import HttpResponse
from django.shortcuts import render, redirect
import pymysql
from app01.students import read_file

DB_HOST = '192.168.14.10'
DB_USER = 'root'
DB_PASSWORD = '1234.Com'
DB_NAME = 'book'


# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 连接数据库
        conn = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        # 创建一个操作数据库的指针
        cursor = conn.cursor()
        sql = "select password from User where username='{}'".format(username)
        cursor.execute(sql)
        res = cursor.fetchone()
        if res is None or password not in res:
            return render(request, 'login.html', context={'error': '用户名或密码错误'})
        else:
            return render(request, 'img_test.html')


def img_test(request):
    return render(request, 'img_test.html')


def css_test(request):
    return render(request, 'css_test.html')


def student(request):
    # 1. 准备数据
    path = r"F:\projects\Projects\django_study\app01\students.txt"
    students = read_file(path)
    # print(students)
    # 2. 用获得的数据填充HTML
    return render(request, 'students.html', context={"data": students})


def testdb(request):
    conn = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    return HttpResponse('连接成功！')


def book(request):
    # 连接数据库
    conn = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    # 创建一个操作数据库的指针
    cursor = conn.cursor()

    if request.method == "GET":

        # 获取数据库的数据
        # 准备SQL语句
        sql = "select BookId,BookName,TypeName,AuthorName,PressName,BookPrice,BookSumNo,AuthorID " \
              "from Book INNER JOIN BookType on Book.BookTypeID = BookType.ID " \
              "INNER JOIN Author on Book.BookAuthor = Author.AuthorID " \
              "Inner Join Press  on Book.BookPressID = Press.PressID "

    else:
        bookid = request.POST.get('bookid')
        # 连接数据库获取当前bookid的值
        sql = "select BookId,BookName,TypeName,AuthorName,PressName,BookPrice,BookSumNo " \
              "from Book INNER JOIN BookType on Book.BookTypeID = BookType.ID " \
              "INNER JOIN Author on Book.BookAuthor = Author.AuthorID " \
              "Inner Join Press  on Book.BookPressID = Press.PressID " \
              "Where BookId = '%s'" % (bookid)
    # 展示数据
    cursor.execute(sql)
    results = cursor.fetchall()
    return render(request, 'book.html', context={"data": results})


def author(request, author_id=0):
    conn = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cursor = conn.cursor()
    if author_id == 0:
        sql = "select AuthorID,AuthorName,AuthorAge,AuthorCity,AuthorTelNo,AuthorEMail,AuthorWorkAddress" \
              " from Author"
        cursor.execute(sql)
        results = cursor.fetchall()
        return render(request, 'author.html', context={'data': results})
    else:
        sql = "select AuthorID,AuthorName,AuthorAge,AuthorCity,AuthorTelNo,AuthorEMail,AuthorWorkAddress" \
              " from Author where AuthorID = {}".format(author_id)
        cursor.execute(sql)
        results = cursor.fetchall()
        return render(request, 'author.html', context={'data': results})


def test(request, id):
    text = 'hello' + str(id)
    return HttpResponse(text)


def book_details(request, book_id):
    # 连接数据库
    conn = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    # 创建一个操作数据库的指针
    cursor = conn.cursor()
    sql = "SELECT BookID,BookName,BookTypeID,BookAuthor,BookPrice,BookPressID,BookSumNo " \
          "FROM Book " \
          "WHERE BookID={}".format(book_id)
    cursor.execute(sql)
    result = cursor.fetchone()
    return render(request, 'book_detail.html', context={'data': result})


def book_add(request):
    if request.method == "GET":
        return render(request, 'book_add.html')
    elif request.method == "POST":
        book_id = request.POST.get('book_id')
        book_name = request.POST.get('book_name')
        book_type = request.POST.get('book_type')
        book_author = request.POST.get('book_author')
        book_price = request.POST.get('book_price')
        book_press = request.POST.get('book_press')
        book_num = request.POST.get('book_num')
        # 连接数据库
        conn = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        # 创建一个操作数据库的指针
        cursor = conn.cursor()

        sql = "INSERT INTO Book (BookID,BookName,BookTypeID,BookAuthor,BookPrice,BookPressID,BookSumNo) " \
              "VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(book_id, book_name, book_type, book_author,
                                                                   book_price, book_press, book_num)
        cursor.execute(sql)
        conn.commit()
        return redirect('/book')


def book_modify(request, book_id):
    # 连接数据库
    conn = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    # 创建一个操作数据库的指针
    cursor = conn.cursor()

    if request.method == "GET":
        sql = "SELECT BookID,BookName,BookTypeID,BookAuthor,BookPrice,BookPressID,BookSumNo " \
              "FROM Book " \
              "WHERE BookID={}".format(book_id)
        cursor.execute(sql)
        result = cursor.fetchone()
        return render(request, 'book_modify.html', context={'data': result})
    elif request.method == "POST":
        book_name = request.POST.get('book_name')
        book_type = request.POST.get('book_type')
        book_author = request.POST.get('book_author')
        book_price = request.POST.get('book_price')
        book_press = request.POST.get('book_press')
        book_num = request.POST.get('book_num')

        sql = "UPDATE Book SET BookName='{}',BookTypeID='{}',BookAuthor='{}'," \
              "BookPrice='{}',BookPressID='{}',BookSumNo='{}' WHERE BookID='{}'" \
            .format(book_name, book_type, book_author, book_price, book_press, book_num, book_id)
        print(sql)
        cursor.execute(sql)
        conn.commit()
        return redirect('/book')


def book_delete(request, book_id):
    # 连接数据库
    conn = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    # 创建一个操作数据库的指针
    cursor = conn.cursor()
    sql = "DELETE FROM Book WHERE BookID={}".format(book_id)
    print(sql)
    cursor.execute(sql)
    conn.commit()
    return redirect('/book')
