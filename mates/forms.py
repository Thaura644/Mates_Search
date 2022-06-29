from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    university = forms.CharField()

    class Meta:
        model = User
        fields = ('username','email','university','password')




