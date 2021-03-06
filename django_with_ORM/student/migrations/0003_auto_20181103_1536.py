# Generated by Django 2.1.3 on 2018-11-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('bookname', models.CharField(max_length=100)),
                ('booktype', models.CharField(max_length=100)),
                ('bookauthor', models.CharField(max_length=100)),
                ('bookpress', models.CharField(max_length=100)),
                ('bookprice', models.CharField(max_length=100)),
                ('booknumber', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowdate', models.DateField()),
                ('returndate', models.DateField()),
                ('bookid', models.ForeignKey(on_delete=None, to='student.Book')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=100, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=100, unique=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=4, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.CharField(max_length=100, unique=True, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sno',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='学号'),
        ),
        migrations.AddField(
            model_name='borrowbook',
            name='sno',
            field=models.ForeignKey(on_delete=None, to='student.Student'),
        ),
    ]
