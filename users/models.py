from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    
    USER_TYPES = (
                ('manager', 'Manager'),
                ('staff', 'Staff'),
                ('collector', 'Collector'),
                ('customer', 'Customer'),
                )
        
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='manager')
    is_manager = models.BooleanField(default=False)
    is_collector = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    username = models.CharField(max_length=255 , null=False , unique=True)
    email = models.CharField(max_length=254 , unique=True)
    password = models.CharField(max_length=50)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []