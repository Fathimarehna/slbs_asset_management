from django.db import models

# Create your models here.
       
class Asset(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE, related_name='categories')
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    category=models.ForeignKey('Category',on_delete=models.CASCADE,related_name='subcategories')
    title=models.CharField(max_length=200)
    status=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Department(models.Model):
    title=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Location(models.Model):
    location=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location



class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'user'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    password = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
