from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.

class User(AbstractUser):
    
    usertypelist = {
        ('customer' , 'customer'),
        ('staff' , 'staff'),
        ('manager' , 'manager'),
    }
    
    usertype = models.CharField(max_length=10 , choices=usertypelist , default='customer')
    email = models.EmailField(unique=True)
    is_collector = models.BooleanField(default=False)

    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        super().save(*args, **kwargs)