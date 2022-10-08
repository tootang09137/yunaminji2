from django.shortcuts import render, redirect, get_object_or_404
from .forms import CashbookForm
from django.utils import timezone
from .models import Cashbook
from django.contrib.auth.forms import AuthenticationForm
from account.models import CustomUser
from django.contrib.auth import authenticate
# Create your views here.

def main(request):
    return render(request, 'main.html')

def write(request):
    user = request.user
    user_id = str(user.id)
    if (user.is_authenticated == True) and (user_id == id):
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return render(request, 'write.html')
    else:
        form = AuthenticationForm()
        context = {
            'form':form
        }
    return render(request, 'login.html', context)

        
def read(request):
    cashbooks = Cashbook.objects
    return render(request, 'read.html', {'cashbooks':cashbooks})

def detail(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    return render(request, 'detail.html', {'cashbooks':cashbooks})

def edit(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    if request.method == "POST":
        form = CashbookForm(request.POST, instance=cashbooks)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')

    else:
        form = CashbookForm(instance=cashbooks)
        return render(request, 'edit.html', {'form':form, 'cashbooks':cashbooks})

def delete(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    cashbooks.delete()
    return redirect('read')
