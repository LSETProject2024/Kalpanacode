from django.contrib import admin
from django.urls import path
from dbapp import views

urlpatterns = [
    path('get_customers', views.get_customers,name = 'get_customers'),
    path('get_authentication', views.get_authentication,name = 'get_authentication'),
    path('get_payment', views.get_payment,name = 'get_payment'),
    ]

