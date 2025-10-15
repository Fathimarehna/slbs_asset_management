from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name="login"),

    path('adminhome/',views.admin_dashboard,name="admin_dashboard"),
    path('userhome/',views.user_dashboard,name="user_dashboard"),
    path('usermanagement/',views.usermanagement,name="usermanagement"),

]

    
