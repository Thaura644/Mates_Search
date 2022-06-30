from django.shortcuts import render,redirect
from django.http import HttpResponse

def user_login(request):
    context = {}
    return render(request,'registration/login.html',context)

def user_registration(request):
    context = {}
    return render(request,'sign-up.html',context)


def discover(request):
    context = {}
    return render(request, 'discover.html', context)


def notifications(request):
    context = {}
    return render(request,'notifications.html',context)
def default_page(request):
    context = {}
    return render(request,'default-page.html',context)

def Profile(request):
    context = {}
    return render(request,'profile.html',context)

