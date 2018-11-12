from django.db import models


# Create your models here.

# 创建一个测试表---T1
class T1(models.Model):
    name = models.CharField(max_length=100, null=False)
    gender = models.CharField(max_length=100, null=True)
    birthday = models.DateField(null=True)
    mobile = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    desc = models.TextField()


class Student(models.Model):
    sno = models.IntegerField(u'学号', primary_key=True)
    name = models.CharField(u'姓名', max_length=100, null=False)
    gender = models.CharField(u'性别', max_length=4, null=False)
    birthday = models.DateField(u'生日', null=True)
    mobile = models.CharField(u'手机号码', max_length=100, unique=True)
    email = models.CharField(u'邮箱', max_length=100, unique=True)
    address = models.CharField(u'地址', max_length=100)


class Book(models.Model):
    bookid = models.CharField(max_length=100,primary_key=True)
    bookname = models.CharField(max_length=100,null=False)
    booktype = models.CharField(max_length=100,null=False)
    bookauthor = models.CharField(max_length=100,null=False)
    bookpress = models.CharField(max_length=100,null=False)
    bookprice = models.CharField(max_length=100,null=False)
    booknumber = models.CharField(max_length=100,null=False)


class BorrowBook(models.Model):
    sno = models.ForeignKey(to="Student",on_delete=None)
    bookid = models.ForeignKey(to="Book", on_delete=None)
    borrowdate = models.DateField()
    returndate = models.DateField()
