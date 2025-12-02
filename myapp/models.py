from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
       
class Asset(models.Model):
    title = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    asset = models.OneToOneField('Asset', on_delete=models.CASCADE, related_name='category')
    # asset = models.ForeignKey('Asset', on_delete=models.CASCADE, related_name='categories')
    title = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    category=models.ForeignKey('Category',on_delete=models.CASCADE,related_name='subcategories')
    title=models.CharField(max_length=20)
    status=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Department(models.Model):
    title=models.CharField(max_length=20)
    status=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Location(models.Model):
    location=models.CharField(max_length=20)
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

    name = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    password = models.CharField(max_length=12)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name





class AssetCreate(models.Model):
    CONDITION_CHOICES=[('Good','Good'),('Fair','Fair'),('Poor','Poor')]
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    subcategory=models.ForeignKey('SubCategory',on_delete=models.CASCADE)
    assetname=models.CharField(max_length=30)
    description=models.CharField(max_length=1000)
    make=models.CharField(max_length=10)
    location=models.ForeignKey('Location',on_delete=models.CASCADE)
    assigned_to=models.CharField(max_length=50)
    department=models.ForeignKey('Department',on_delete=models.CASCADE)
    purchase_date=models.DateField()
    warrenty_expiry=models.DateField()
    condition=models.CharField(max_length=10,choices=CONDITION_CHOICES)
    remarks=models.TextField(max_length=1000)
    status=models.BooleanField(default=True)
    file = models.FileField(upload_to='asset_files/', blank=True, null=True)









 

