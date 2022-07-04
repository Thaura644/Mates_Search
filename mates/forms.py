from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Notifications

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    university = forms.CharField()

    class Meta:
        model = User
        fields = ('username','email','university','password')

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

                
        
        




