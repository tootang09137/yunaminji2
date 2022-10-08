from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from account.forms import CustomUserCreationForm 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from account.forms import CustomUserCreationForm
from .forms import CustomUser
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('login')
        else:
            return render(request, 'signup.html', {'form':form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form':form})

def login(request):
    if request.method =='POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})


def logout(request):
    auth.logout(request)
    return redirect('main')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('main')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})