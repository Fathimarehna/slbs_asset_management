from django import forms
from django.contrib.auth.models import User
from . models import Asset
from .models import Category
from .models import SubCategory
from .models import Department
from .models import Location
from .models import User

class AssetForm(forms.ModelForm):
    class Meta:
        model=Asset
        fields = [ 'title']




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['asset', 'title']



class SubCategoryForm(forms.ModelForm):
    class Meta:
        model=SubCategory
        fields=['category','title']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title']
class LocationForm(forms.ModelForm):
    class Meta:
        model=Location
        fields=['location']
   

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'role', 'password']

   


  


    
