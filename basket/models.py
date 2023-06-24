from django.db import models
from django.contrib.auth.models import User
from shop.models import Brawl
import datetime

# Create your models here.

#Модель для промежуточной таблицы Корзины
class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brawl = models.ForeignKey(Brawl, on_delete=models.CASCADE)

#Модель для Заказа
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.CharField(max_length=300)
    CVC = models.IntegerField()
    city = models.CharField(max_length=300)
    datetime = models.DateField(default=datetime.datetime.now().strftime("%Y-%m-%d"))
    all_price = models.FloatField()