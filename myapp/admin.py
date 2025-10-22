from django.contrib import admin

# Register your models here.

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'created_date', 'updated_date')
    search_fields = ('name', 'role')
