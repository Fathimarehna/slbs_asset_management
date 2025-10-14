from django.shortcuts import render, redirect
from .models import User, Asset
from .forms import RegisterForm, LoginForm, AssetForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email, password=password)
                request.session['user_id'] = user.id
                request.session['user_role'] = user.role
                if user.role == 'Admin':
                    return redirect('admin_dashboard')
                else:
                    return redirect('user_dashboard')
            except User.DoesNotExist:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    request.session.flush()
    return redirect('login')


def admin_dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login')
    user = User.objects.get(id=request.session['user_id'])
    if user.role != 'Admin':
        return redirect('user_dashboard')
    assets = Asset.objects.all()
    return render(request, 'admin_dashboard.html', {'user': user, 'assets': assets})




def user_dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login')
    user = User.objects.get(id=request.session['user_id'])
    assets = Asset.objects.filter(created_by=user)
    return render(request, 'user_dashboard.html', {'user': user, 'assets': assets})

def create_asset(request):
    if 'user_id' not in request.session:
        return redirect('login')
    user = User.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.created_by = user
            asset.save()
            if user.role == 'Admin':
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
    else:
        form = AssetForm()
    return render(request, 'create_asset.html', {'form': form})

