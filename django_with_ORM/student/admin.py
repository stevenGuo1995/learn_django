from django.contrib import admin
from . import models


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('sno', 'name', 'gender', 'birthday', 'mobile', 'email', 'address')


# 把某一个表加入后台接受管理
admin.site.register(models.Student)
