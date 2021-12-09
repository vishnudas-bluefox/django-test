from django.contrib import admin
from django.urls import path,include
from . import views


app_name = 'test1'
urlpatterns = [
    path('', views.main,name='index'),
    path('CS/', views.CS,name='CS'),
    path('IT/', views.IT,name='IT'),
    path('EEE/', views.EEE,name='EEE'),
    path('EC/', views.EC,name='EC'),
    path('MECH/', views.MECH,name='MECH'),
    path('star/', views.star,name='star'),
]
