from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            user = forms.save()
            login(request, user)
            messages.success(request, 'Registration done successfully and logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Registration failed.. Try again!')
    else:
        form =RegistrationForm()
    return render(request, 'accounts/register.html', {'form' : form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully")
            return redirect('dashboard')

        else:
            messages.error(request, 'Login failed')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')


@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')

