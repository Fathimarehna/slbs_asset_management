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

    # path('create_user/', views.create_user, name='user'),
    # path('users/', views.users_view, name='users'),
    # path('users_list/',views.users_list,name='users_list'), 
    # path('categories/update/<int:pk>/', views.user_update, name='user_update'),
    # path('categories/delete/<int:pk>/', views.user_delete, name='user_delete'),  
    # path('category/toggle/<int:pk>/', views.toggle_user_status, name='toggle_user_status'),
    # path('add_user/', views.add_user_view, name='add_user'),
     path('users/', views.users_view, name='users'),
    path('add_user/', views.add_user, name='add_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]

    
