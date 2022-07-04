from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterUserForm,ProfileForm
from .models import Notifications,CustomUser
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_str
from django.utils.http  import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .token import account_activation_token
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfully")   
            return redirect('notifications') 
        else:
            messages.success(request,"Incorrect username or password")   
            return redirect('login') 
               
    else :
         return render(request,'registration/login.html', {'error_message': 'Something went wrong.Try Again'})
def logout_user(request):
	logout(request)
	messages.success(request,"You have succefully logged out")
	return redirect('login')
def user_registration(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        
        if form.is_valid():
            """ 
            user = form.save(commit=False)
            user.is_active=False
            user.save()#saves user in memory not database
            current_url=get_current_site(request)
            mail_subject = "Activation Link has been sent to your Email Address"
            message = render_to_string("email.html",{
                'user':user,
                'domain':current_url.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject,message,to=[to_email]
            )
            email.send()
            messages.success(request,"Activation link has been sent to your email")
            return redirect('register') 
            """
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            post_email = form.cleaned_data['email']
            user.save()
            user = authenticate(username=username,password=password)
            if user is not None and CustomUser.objects.filter(email=post_email).exists()==False:
                login(request, user)
                Notifications.objects.create(user_id=request.user.id,title="Welcome to Mates Search",details="Stop the search and find your soul mate at an instant")
                messages.success(request,"Your account has successfully been created")
                return redirect('login')
            else:
                messages.success(request,"Account already exists")
                return redirect('register')

            

        else:
            messages.success(request,"Fill your registration details correctly")
            return redirect('register') 
                
            #Notifications.object.create(user_id=request.user.id,title="Welcome to Mates Search"
            #sentTime=,details="Stop the search and find your soul mate at an instant")
    else:
        form = RegisterUserForm()
        return render(request,'sign-up.html',{"form":form})
def activate(request,uidb64,token):
    User = get_user_model()
    try:
        uid= force_str(urlsafe_base64_decode(uidb64))
        user=User.object.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active =True
        user.save()
        messages.success(request,"Thank you for confirming your email")
        return redirect('login')
    else:
        messages.success(request,"Activating account failed")
        return redirect('login')


@login_required
def notifications(request):
    notifications_data = []
    user_id = request.user.id
    notifications = Notifications.objects.select_related().filter(user_id=user_id)
    for notification in notifications:
        data = {"title":notification.title,"timeSent":notification.sentTime,"details":notification.details}
        notifications_data.append(data)
    response = JsonResponse(notifications_data,content_type='application/json',safe=False)
    print(notifications_data)
    return render(request, 'notifications.html',{'notificationsJSON': response})

@login_required     
def profile(request):
    return render(request,'profile.html')
    
