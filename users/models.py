from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
from django.contrib.auth.hashers import make_password

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if not username:
            raise ValueError('The Username field must be set.')
        if not email:
            raise ValueError('The Email field must be set.')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 'manager')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    
    USER_TYPES = (
                ('manager', 'Manager'),
                ('staff', 'Staff'),
                ('collector', 'Collector'),
                ('customer', 'Customer'),
                )
    
        
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='manager')
    username = models.CharField(max_length=255 , null=False , unique=True)
    email = models.CharField(max_length=254 , unique=True ,null=False)
    password = models.CharField(max_length=100)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = CustomUserManager()
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        super().save(*args, **kwargs)
        
    def get_customer_usernames(cls):
        return cls.objects.filter(user_type='customer').values_list('username', flat=True)