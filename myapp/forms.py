from django import forms
<<<<<<< HEAD
from django.contrib.auth.models import User

class UsercreationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    Class Meta:
    

    
=======
from .models import User, Asset

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'role']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            'category', 'sub_category', 'asset_name', 'make_model',
            'serial_number', 'location', 'assigned_to', 'department',
            'purchase_date', 'warranty_expiry', 'condition', 'remarks'
        ]
>>>>>>> e8a5c04a1a4cfe8ea6cc7862e7250e109c836771
