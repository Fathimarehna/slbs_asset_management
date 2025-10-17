from django import forms
from django.contrib.auth.models import User
from . models import Asset
from .models import Category
from .models import SubCategory

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

   

   


  


    
