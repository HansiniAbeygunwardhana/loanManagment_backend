from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User
from .forms import CustomUserChangeForm

# Register your models here.

        
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserChangeForm
    list_display = ['username' , 'email']
    
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email','password1', 'password2')}),
        ('User Type', {'fields': ('user_type',)}),
        
    )
    
admin.site.register(User , CustomUserAdmin)