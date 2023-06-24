from django.urls import path, re_path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search,name='searchbar'),
    path('contacts/', views.contacts,name='contacts'),
    path('<character_slug>/',views.index, name='company_sort'),
    path('brawl/<brawl_slug>', views.brawl, name='brawl_page'),
]