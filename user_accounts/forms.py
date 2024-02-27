from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from django import forms

class Register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

# letting user to change their info 

class user_change_form(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']