from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name="home"),
    path('information', views.information, name="information"),
    path('menu/', views.menu, name="menu"),
    path('typesofdishes/', views.typesofdishes, name="typesofdishes"),
    path('dish/<str:pk>/', views.dishinfo, name="dishinfo"),
    path('sale/', views.sale, name="sale"),
    path('sale/<str:pk>/', views.saleinfo, name="saleinfo"),


]