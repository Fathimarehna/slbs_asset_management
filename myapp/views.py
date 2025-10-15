from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

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


def usermanagement(request):
    users = User.objects.all().order_by('id')  # admin will be the first user (id=1)
    return render(request, 'usermanagement.html',{})



