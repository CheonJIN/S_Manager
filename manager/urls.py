'''
Created on 2019. 9. 19.

@author: jhcheon
'''
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.customer_list, name='customer_list'),
    path('', views.home, name='home'),
    path('customer/list/', views.customer_list, name='customer_list'),
    path('customer/new/', views.customer_new, name='customer_new'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('company/list/', views.company_list, name='company_list'),
    path('company/new/', views.company_new, name='company_new'),
    path('company/<int:pk>/edit/', views.company_edit, name='company_edit'),
]