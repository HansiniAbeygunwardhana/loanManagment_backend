from django.db import models
from users.models import User

# Create your models here.
class Customer(User):
    
    name = models.CharField(max_length=100, null=False, unique=True)
    surname = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    telephone1 = models.CharField(max_length=100, null=False)
    telephone2 = models.CharField(max_length=100, null=False)
    dateofbirth = models.DateTimeField(null=True)
    nicnumber = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.username
    