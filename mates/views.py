from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('notifications') 
        else:
            messages.info(request,"Incorrect username or password")   
            return redirect('login') 
               
    else :
         return render(request,'registration/login.html', {'error_message': 'Something went wrong.Try Again'})
def logout_user(request):
	logout(request)
	messages.success(request,"You have succefully logged out")
	return render(request,'home.html')
def user_registration(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request,"Your account has successfully been created")
            return render(request,'login.html')
    context = {}
    return render(request,'sign-up.html',context)

@login_required
def notifications(request):
    context = {}
    return render(request,'notifications.html',context)