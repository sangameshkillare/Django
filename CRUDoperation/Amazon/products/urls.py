from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('edit/<int:id>',views.product_list,name='product_list'),
    path('add/',views.add_product,name='add_product'),
    path('delete/<int:id>',views.product_list,name='product_list'),
    
]