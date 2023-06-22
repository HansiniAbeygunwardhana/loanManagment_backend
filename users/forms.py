from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserChangeForm(UserCreationForm):
    
    email : forms.EmailField()

    class Meta:
        model = User
        exclude = ('password1', 'password2')