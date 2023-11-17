from django import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.forms.widgets import PasswordInput,TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
class loginform(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())