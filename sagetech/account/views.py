from django.shortcuts import render,redirect
from .forms import *
from django.forms import inlineformset_factory
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .mydecorators import anonymous, allowed_users, admin_only

from django.contrib import messages
# Create your views here.

@anonymous
def loginUser(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'Password or Username may be incorrect')
    
    
    datas = {
        
    }
    return render(request, 'login.html')


@anonymous
def registerUser(request):
    form = CreateUser()
    
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid:
            user = form.save()
            
            
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='visiteur')
            user.group.add(group)
            Profile.objects.create(user=user, username=username, email=form.cleaned_data.get('email'))
            messages.success(request, f'+ Account {username} successfully  created')
            return redirect('index')
    
    
    datas={
        'form':form
    }
    return render(request, 'register.html', datas)


def forgot(request):
    datas = {
        
    }
    return render(request, 'forgot-password.html', datas)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')