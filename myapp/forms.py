from django import forms
from django.contrib.auth.models import User

class UsercreationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    Class Meta:
    

    
