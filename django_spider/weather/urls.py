from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('insert/', views.insert_weather_into_db),
    path('echarts/',views.echarts_demo01)
]
