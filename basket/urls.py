from django.urls import path, re_path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.baskets, name='basket'),
    path('order/',views.order_items, name='order'),
]