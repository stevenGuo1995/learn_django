from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('admin/', views.user_admin),
    path('cashier/', views.user_cashier),
    path('storage/', views.user_storage),
    path('cashier/add/', views.product_add),
    path('cashier/delete/',views.product_del)
]
