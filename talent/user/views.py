from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .forms import RegForm
# Create your views here.

def regView(request):
    if request.method=='POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'Registration success')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
            
    else:
        form = RegForm()
    return render(request,'reg.html',{'form':form})

def loginView(request):
    if request.method=='POST':
        username = request.POST['username']
        password =request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password')
            redirect('login')  
    return render(request,'login.html')     
