from django.db import models

# Create your models here.
class customer(models.Model):
    customer_id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=100 , null=False , unique=True)
    surname = models.CharField(max_length=100 , null=False)
    username = models.CharField(max_length=100 , null=False , default=name)
    address = models.CharField(max_length=100 , null=False)
    telephone1 = models.CharField(max_length=100 , null=False)
    telephone2 = models.CharField(max_length=100 , null=False)
    email = models.CharField(max_length=100 , null=False)
    dateofbirth = models.DateField(null=True)
    nicnumber = models.CharField(max_length=100 , null=False)
    
    def __str__(self):
        return self.username
    