from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

#Модель профиля
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    number = models.CharField(max_length=12,null=True)
    birth_date = models.DateField(null=True)
    
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
# Create your models here.
