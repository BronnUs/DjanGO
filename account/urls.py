from django.urls import path, re_path
from . import views

app_name = 'account'

urlpatterns = [
    path('<username>',views.profile_pg,name='profile_pg'),
    path('registration/', views.register,name='register'),
    path('login/',views.my_login,name='login'),
    path('logout/',views.my_logout,name='logout'),
    path('change/', views.profileChange,name='change'),
]