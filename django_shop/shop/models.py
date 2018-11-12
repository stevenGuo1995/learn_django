from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100, null=False)


class Product(models.Model):
    product_id = models.CharField(primary_key=True, max_length=100)
    product_name = models.CharField(max_length=100, null=False)
    product_unit = models.CharField(max_length=100, null=False)
    product_price = models.FloatField(null=False)
    product_category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    product_inventory = models.IntegerField(default=50)


class SalesList(models.Model):
    serial_num = models.CharField(primary_key=True, max_length=100)
    total_num = models.IntegerField(null=False)
    total_money = models.FloatField(null=False)
    receive_money = models.FloatField(null=False)
    return_money = models.FloatField(null=False)
    username = models.CharField(null=False, max_length=100)
    buy_date = models.DateTimeField(auto_created=True)


class SalesListDetail(models.Model):
    serial_num = models.ForeignKey('SalesList', on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100,null=False)
    product_name = models.CharField(max_length=100,null=False)
    product_unit = models.CharField(max_length=100, null=False)
    product_price = models.FloatField(null=False)
    product_num = models.IntegerField(null=False)
    total_money = models.FloatField(null=False)

