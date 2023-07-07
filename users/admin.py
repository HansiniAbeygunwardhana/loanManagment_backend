from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User
from django import forms

# Register your models here.

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        # Set the maximum character limit for the password field
        widgets = {
            'password': forms.PasswordInput(attrs={'maxlength': '200'}),
        }



        
class CustomUserAdmin(UserAdmin):
    
    form = CustomUserChangeForm
    add_form = CustomUserChangeForm
    list_display = ['username' , 'email']
    
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email','password1', 'password2', 'is_staff' ,'is_superuser')}),
        ('User Type', {'fields': ('user_type',)}),
        
    )
    

admin.site.register(User)