from django.db import models
from django.shortcuts import render,reverse, get_object_or_404
# Create your models here.


class Character(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('shop:company_sort',
                        args=[self.slug])

           

class Brawl(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)
    image = models.ImageField(upload_to='django_lab/media/')
    price = models.IntegerField()
    available = models.BooleanField()
    views_count = models.IntegerField()
    order_count = models.IntegerField()
    
    def __str__(self):
        return self.character.title + ' ' + self.name
    
    def get_absolute_url(self):
        return reverse('shop:brawl_page',
                       args=[self.slug])

