from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, PasswordChangeCustomForm, CustomUserCreationForm
from .models import CustomUser

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username1 = request.POST["username"]
            password1 = request.POST["password"]
            user = authenticate(request, username=username1, password=password1)
            if user is not None:
                login(request, user)
                messages.success(request, "تم الدخول بنجاح")
                return redirect('/')  # Replace 'home' with your desired redirect URL
            else:
                messages.error(request, "Invalid username or password")
                return redirect('login')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeCustomForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep user logged in after password change
            messages.success(request, 'Password changed successfully.')
            return redirect('home')
    else:
        form = PasswordChangeCustomForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def deactivate_user(request):
    if request.method == 'POST':
        user = request.user
        user.is_active = False
        user.save()
        logout(request)
        messages.info(request, 'Your account has been deactivated.')
        return redirect('login')
    return render(request, 'deactivate_user.html')

@login_required
def register_user(request):
    form = CustomUserCreationForm(request.POST)
    return render(request, 'register_user.html', {'form': form})


