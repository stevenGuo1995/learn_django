from django.db import models
import datetime


# Create your models here.
class ProvinceURL(models.Model):
    province_id = models.AutoField(primary_key=True)
    province_name = models.CharField(max_length=100, null=False)
    province_url = models.CharField(max_length=100, null=False)


class Weather(models.Model):
    date = models.DateTimeField(null=False)
    city = models.CharField(max_length=100, null=False)
    province_name = models.CharField(max_length=100, null=False)
    weather = models.CharField(max_length=100, null=False)
    max_temp = models.IntegerField(null=False)
    min_temp = models.IntegerField(null=False)
