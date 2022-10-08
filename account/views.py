from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from account.forms import CustomUserCreationForm 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .forms import CustomUser, CustomUserChangeForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('mypage', user.id)
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
            return render(request, 'mypage.html', {'form':form})
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

def mypage(request, id):
    user = request.user
    user_id = str(user.id)
    if (user.is_authenticated == True) and (user_id == id) :
        user = CustomUser.objects.get(id=id)
        context = {
            'user':user,
        }
        return render(request, 'mypage.html', context)
    else:
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'login.html', context)

def user_change(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('main')
    else : 
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'user_change.html', context)

def signup_yuna(request):
    return render(request, 'accout/signup_yuna.html')