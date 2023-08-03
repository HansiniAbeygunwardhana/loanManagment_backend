# yourapp/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

# Create a custom form to display only selected fields as write fields
class CustomUserForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'password', 'email', 'usertype', 'is_collector')

# Create a custom UserAdmin class to customize the Django admin view
class CustomUserAdmin(UserAdmin):
    form = CustomUserForm

    # Fields to be displayed in the main view (write fields)
    list_display = ('username', 'email', 'usertype', 'is_collector' , 'date_joined', 'is_active')

    # Fields to be shown when adding/editing a user (write fields)
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email', 'usertype', 'is_collector' , 'date_joined', 'is_active')
        }),
    )

    # Fields to be displayed in a submenu (readonly fields)
    readonly_fields = ('id',  'last_login')

    # Add the submenu and move the readonly fields into it
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        readonly_fieldsets = (
            ('Login and OtherData', {
                'fields': ('id',  'last_login'),
                'classes': ('collapse', 'collapse-closed'),
            }),
        )
        return fieldsets + readonly_fieldsets

# Register the CustomUser model with the custom admin view
admin.site.register(CustomUser, CustomUserAdmin)
