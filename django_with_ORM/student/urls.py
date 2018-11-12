from django.urls import path
from . import views

urlpatterns = [
    path('save/', views.save_data),
    path('index/', views.index),
    path('stu_add/', views.stu_add),
    path('stu_modify/<int:sno>/', views.stu_modify),
    path('stu_detail/<int:sno>/', views.stu_detail),
    path('stu_delete/<int:sno>', views.stu_delete)
]

