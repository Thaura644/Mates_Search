from django.shortcuts import render, redirect


def home(request):
    context = {}
    return render(request, 'home.html', context)


def discover(request):
    context = {}
    return render(request, 'discover.html', context)


def messages(request):
    context = {}
    return render(request, 'messages.html', context)


def profile(request):
    context = {}
    return render(request, 'profile.html', context)
