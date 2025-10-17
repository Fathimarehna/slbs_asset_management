from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name="login"),

    path('adminhome/',views.admin_dashboard,name="admin_dashboard"),
    path('userhome/',views.user_dashboard,name="user_dashboard"),


    path('assetid/',views.assetid,name="assetid"),
    path('assets/create/', views.asset_create, name='asset_create'),
    path('assets/update/<int:pk>/', views.asset_update, name='asset_update'),
    path('assets/delete/<int:pk>/', views.asset_delete, name='asset_delete'),
    path('asset/toggle/<int:pk>/', views.toggle_asset_status, name='toggle_asset_status'),
    


    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'), 
    path('categories/update/<int:pk>/', views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),   
    path('category/toggle/<int:pk>/', views.toggle_category_status, name='toggle_category_status'),
]

    
