from django.shortcuts import render,redirect
from . import db
def user_login(request):
    context = {}
    return render(request,'registration/login.html',context)

def user_registration(request):
    context = {}
    return render(request,'sign-up.html',context)

def notifications(request):
    context = {}
    return render(request,'notifications.html',context)