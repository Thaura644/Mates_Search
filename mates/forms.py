from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Notifications,CustomUser

class RegisterUserForm(UserCreationForm):
    gender=(("male",'male'),("female",'female'))
    username = forms.CharField(max_length=50,widget=forms.TextInput(
                attrs={'placeholder': 'Enter Username',
                       'name':'username','id':'username',
                       'class': 'login-name',
                       'required':''}))
    email = forms.EmailField(widget=forms.TextInput(
                attrs={'placeholder': 'Enter Email','type':'email',
                'name':'email','id':'email',
                       'class': 'login-name','required':''}))
    university = forms.CharField(widget=forms.TextInput(
                attrs={'placeholder': 'Enter University','name':'university',
                'id':'university','class': 'login-name','required':''}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password','id':'password1','type':'password','name':'password1', 'required':''}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password','id':'password2','type':'password','name':'password2', 'required':''}))
 
    gender = forms.ChoiceField(initial="male",choices=gender,widget=forms.Select(
            attrs={'name': 'login-input-gender-id', 'required':''}))

    accept_terms = forms.BooleanField(initial=False)
    class Meta:
        model = CustomUser
        fields = ('username','email','university','password1','password2','gender','accept_terms')

"""  def __init__(self,*args,**kwargs):
        super().__init__(*args,*kwargs)
        gender=((0,'male'),(1,'female'))
        username = forms.CharField(max_length=50,required=True,widget=forms.TextInput(
                attrs={'placeholder': 'Enter Username',
                       'class': 'login-name'}))
        email = forms.EmailField(required=True,widget=forms.TextInput(
                attrs={'placeholder': 'Enter Email','type':'email',
                       'class': 'login-name'}))
        university = forms.CharField(required=True,widget=forms.TextInput(
                attrs={'placeholder': 'Enter University',
                       'class': 'login-name'}))
        gender = forms.ChoiceField(required=True,choices=gender,widget=forms.Select(
            attrs={'name': 'login-input-gender-id'}))
        self.fields['username']= username
        self.fields['email']=email
        self.fields['university'].widget.attrs.update({

        }) 
        self.fields['gender'] = gender"""
"""class NotificationsForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        notifications = Notifications.objects.select_related().filter(
            user_id=user)
        cluster = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'data-parsley-required': 'true',
                   'id': 'cluster'}))"""

class ProfileForm(forms.Form):
    """Profile Form"""
    def __init__(self, user, *args, **kwargs):
        self.user  = user

                
        
        
class UpdateProfileForm1(forms.Form):
    location
    class Meta:
        model = CustomUser
        fields = ('location','phone_number','height','date_of_birth','email','status','university','gender')




