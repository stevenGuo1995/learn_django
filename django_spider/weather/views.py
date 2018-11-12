from django.shortcuts import render
from django.http import HttpResponse
from . import spider_china_weather as weather
from . import models
import datetime


# Create your views here.

def index(request):
    return HttpResponse('hey! there!')


def insert_weather_into_db(request):
    url = 'http://www.nmc.cn/publish/forecast/china.html'
    province_all = weather.get_china_by_url(url)
    for province in province_all:
        keys = list(province.keys())
        print(province)
        obj_province = models.ProvinceURL(
            province_name=keys[0],
            province_url=province['provinceURL']
        )
        obj_province.save()
        for city in province[keys[0]]:
            print(city)
            obj_weather = models.Weather(
                date=datetime.datetime.today() - datetime.timedelta(days=1),
                city=city['city'],
                province_name=keys[0],
                weather=city['weather'],
                max_temp=int(city['max_temp']),
                min_temp=int(city['min_temp'])
            )
            obj_weather.save()

    return HttpResponse('insert success!')


def echarts_demo01(request):
    return render(request, 'weather/echarts_study01.html')
