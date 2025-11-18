from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.login_view,name="login"),

    path('adminhome/',views.admin_dashboard,name="admin_dashboard"),
    path('userhome/',views.user_dashboard,name="user_dashboard"),
    path('logout',views.logout_view,name='logout'),


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


    path('subcategories/', views.subcategory_list, name='subcategory_list'),
    path('subcategories/create/', views.subcategory_create, name='subcategory_create'),
    path('subcategories/update/<int:pk>/', views.subcategory_update, name='subcategory_update'),
    path('subcategories/delete/<int:pk>/', views.subcategory_delete, name='subcategory_delete'),   
    path('subcategory/toggle/<int:pk>/', views.toggle_subcategory_status, name='toggle_subcategory_status'),


    path('departments/', views.departments_list, name='departments_list'),
    path('departments/create/', views.departments_create, name='departments_create'),
    path('departments/update/<int:pk>/', views.departments_update, name='departments_update'),
    path('departments/delete/<int:pk>/', views.departments_delete, name='departments_delete'),   
    path('departments/toggle/<int:pk>/', views.toggle_departments_status, name='toggle_departments_status'),


    path('locations/', views.locations_list, name='locations_list'),
    path('locations/create/', views.locations_create, name='locations_create'),
    path('locations/update/<int:pk>/', views.locations_update, name='locations_update'),
    path('locations/delete/<int:pk>/', views.locations_delete, name='locations_delete'),   
    path('locations/toggle/<int:pk>/', views.toggle_locations_status, name='toggle_locations_status'),
   
    path('users/', views.users_view, name='users'),
    path('add_user/', views.add_user, name='add_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),


    path('assetform/', views.assetformlist, name='assetlist'),
    path('assets/assetform', views.assetformcreate, name='assetformcreatepage'),
    path('assetform/update/<int:pk>/', views.assetform_update, name='assetform_update'),
    path('assetform/delete/<int:pk>/', views.assetform_delete, name='assetform_delete'),   
    path('assetform/details/<int:pk>/', views.assetform_details, name='assetform_details'),


    path('assetform/user', views.assetformuser, name='assetformuser'),
    
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),


    path('report/', views.asset_report, name='asset_report'),
    path('assets/create/', views.asset_create, name='assetcreatepage'),

]

    
