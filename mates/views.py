from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm, ProfileForm
from .models import Notifications
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully")
            Notifications.objects.create(user_id=request.user.id, title="Welcome to Mates Search",
                                         details="Stop the search and find your soul mate at an instant")
            return redirect('notifications')
        else:
            messages.success(request, "Incorrect username or password")
            return redirect('login')

    else:
        return render(request, 'registration/login.html', {'error_message': 'Something went wrong.Try Again'})


def logout_user(request):
    logout(request)
    messages.success(request, "You have succefully logged out")
    return render(request, 'home.html')


def user_registration(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, "Your account has successfully been created")
            # Notifications.object.create(user_id=request.user.id,title="Welcome to Mates Search"
            # sentTime=,details="Stop the search and find your soul mate at an instant")
            return render(request, 'login.html')
    context = {}
    return render(request, 'sign-up.html',)


# @login_required
def discover(request):
    context = {}
    return render(request, 'discover.html', context)


def notifications(request):
    notifications = []
    user_id = request.user.id
    notification = Notifications.objects.get(user_id=user_id)
    data = {"title": notification.title,
            "timeSent": notification.sentTime, "details": notification.details}
    notifications.append(data)
    response = JsonResponse(
        notifications, content_type='application/json', safe=False)
    return render(request, 'notifications.html', {'notifications': notifications})


def messages(request):
    context = {}
    return render(request, 'messages.html', context)


def profile(request):
    context = {}
    return render(request, 'profile.html', context)
