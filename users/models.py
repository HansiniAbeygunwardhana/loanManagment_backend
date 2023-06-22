from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.


class User(AbstractUser):
    
    USER_TYPES = (
                ('manager', 'Manager'),
                ('staff', 'Staff'),
                ('collector', 'Collector'),
                ('customer', 'Customer'),
                )
    
        
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='manager')
    username = models.CharField(max_length=255 , null=False , unique=True)
    email = models.CharField(max_length=254 , unique=True)
    password = models.CharField(max_length=100)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        super().save(*args, **kwargs)
        
    def get_customer_usernames(cls):
        return cls.objects.filter(user_type='customer').values_list('username', flat=True)