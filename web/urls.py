"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('',views.main, name="main"),
    path('user_register', views.user_register, name="user_register"),
    path('authentication_login', views.authentication_login, name="authentication_login"),
    path('admin_dashboard', views.admin_dashboard,name="admin_dashboard"),
    path('admin_pg',views.admin_pg,name="admin_pg"),
    path('admin_manage_product',views.admin_manage_product, name="admin_manage_product"),
    path('admin_product_adding',views.admin_product_adding, name="admin_product_adding"),
    path('product_add',views.product_add, name="product_add"),
    path('update_product/<int:id>',views.update_product, name="update_product"),
    path('update_pdt',views.update_pdt, name="update_pdt"),
    path('delete_product/<int:id>',views.delete_product,name="delete_product"),
    path('insert_user',views.insert_user, name="insert_user"),
    path('users_home',views.users_home, name="users_home"),
    path('users_dashboard',views.users_dashboard, name="users_dashboard"),
    path('product_cartlist/<int:id>',views.product_cartlist, name="product_cartlist"),
    path('product_order',views.product_order, name="product_order"),
    path('view_cartlist',views.view_cartlist, name="view_cartlist"),
    path('removes/<int:id>',views.removes, name="removes"),
]
