from django import forms
from django.contrib.auth.models import User
from . models import Asset
from .models import Category
from .models import SubCategory
from .models import Department
from .models import Location
from . models import AssetCreate


from django.core.validators import MinLengthValidator,RegexValidator



class AssetForm(forms.ModelForm):


    title = forms.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(3,message='Minimum 3 charecters required , '),
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message='Only letters, numbers and spaces are allowed.'
            )
        ]
    )
    class Meta:
        model=Asset
        fields = [ 'title']




class CategoryForm(forms.ModelForm):
    title = forms.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(3,message='Minimum 3 charecters required'),
            RegexValidator(
                regex=r'^[A-Za-z ]+$',
                message='Only letters and spaces are allowed.'
            )
        ]
    )
    class Meta:
        model = Category
        fields = ['asset', 'title']



class SubCategoryForm(forms.ModelForm):
    title = forms.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(3,message='Minimum 3 charecters required'),
            RegexValidator(
                regex=r'^[A-Za-z ]+$',
                message='Only letters and spaces are allowed.'
            )
        ]
    )
    class Meta:
        model=SubCategory
        fields=['category','title']


class DepartmentForm(forms.ModelForm):
    title = forms.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(3,message='Minimum 3 charecters required'),
            RegexValidator(
                regex=r'^[A-Za-z ]+$',
                message='Only letters and spaces are allowed.'
            )
        ]
    )
    class Meta:
        model = Department
        fields = ['title']

        
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['name', 'role', 'password']



class LocationForm(forms.ModelForm):


    location = forms.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(3,message='Minimum 3 charecters required , '),
            RegexValidator(
                regex=r'^[A-Za-z ]+$',
                message='Only letters and spaces are allowed.'
            )
        ]
    )
    class Meta:
        model=Location
        fields=['location']

class AssetCreateForm(forms.ModelForm):

    assetname = forms.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(3,message='Minimum 3 charecters required'),
            RegexValidator(
                regex=r'^[A-Za-z ]+$',
                message='Only letters and spaces are allowed.'
            )
        ]
    )


    make = forms.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(3, message='Minimum 3 characters required.'),
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message='Only letters, numbers and spaces are allowed.'
            )
        ]
    )



    class Meta:
        model = AssetCreate
        fields = [
            'category', 'subcategory', 'assetname', 'description','make', 'location',
            'assigned_to', 'department', 'purchase_date', 'warrenty_expiry',
            'condition', 'remarks'
        ]

        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'warrenty_expiry': forms.DateInput(attrs={'type': 'date'}),
            'remarks': forms.Textarea(attrs={'rows': 2}),
        }

    # 👇 This is the function that filters subcategories based on selected category
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initially show no subcategories

        
        self.fields['subcategory'].queryset = SubCategory.objects.none()

        # If a category is selected (user selected in the form)
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass  # ignore if invalid input
        # If editing an existing record, show relevant subcategories
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategories.all()



from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class AddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Passwords do not match. Please try again.")

