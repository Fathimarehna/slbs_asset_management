from django.shortcuts import render, redirect,get_object_or_404

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from . models import Asset
from .forms import AssetForm
from .models import Category
from .forms import CategoryForm
from django.utils import timezone

# Create your views here.


def login_view(request):


    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(username='admin', password='12345678', email='admin@example.com')
        print("Admin user created")


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            

            
            if username == 'admin' and password == '12345678':
                messages.success(request, "Welcome Admin! Login successful.")
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')



@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')



def assetid(request):
    assets = Asset.objects.all()
    return render(request, 'assetid.html', {'assets': assets})


def asset_create(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assetid')
    else:
        form = AssetForm()
    return render(request, 'asset_form.html', {'form': form})

def asset_update(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('assetid')
    else:
        form = AssetForm(instance=asset)
    return render(request, 'asset_form.html', {'form': form})


def asset_delete(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        asset.delete()
        return redirect('assetid')
    return render(request, 'assetconfirmdelete.html', {'asset': asset})

def toggle_asset_status(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    asset.status = not asset.status  # Toggle between active/inactive
    asset.save()
    return redirect('assetid')

def category_list(request):
    categories = Category.objects.select_related('asset').all()
    return render(request, 'category_list.html', {'categories': categories})


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})



def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})


def toggle_category_status(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.status = not category.status  # Toggle between active/inactive
    category.save()
    return redirect('category_list')



from .forms import UserForm

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # redirect to user list page
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})


def toggle_user_status(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.status = not user.status  # Toggle between active/inactive
    user.save()
    return redirect('user')


def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

def user_update(request, pk):
    category = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('users_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'user_form.html', {'form': form})


def user_delete(request, pk):
    users = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
       users.delete()
       return redirect('users_list') 
    return render(request, 'user_confirm_delete.html', {'users': users})

def users_view(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('users')
    return render(request, 'add_user.html')

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        # optional: change password if provided
        new_password = request.POST.get('password')
        if new_password:
            user.set_password(new_password)
        # update the date
        user.last_login = timezone.now()
        user.save()
        return redirect('users')
    return render(request, 'edit_user.html', {'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('users')



