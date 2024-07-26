from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .forms import Reg
# Create your views here.

def regView(request):
    if request.method=='POST'
    form =