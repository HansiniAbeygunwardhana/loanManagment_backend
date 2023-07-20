from django.db import models
from users.models import CustomUser
from cloudinary.models import CloudinaryField

# Create your models here.
class CustomerProfile(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, unique=True)
    surname = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    telephone1 = models.CharField(max_length=100, null=False)
    telephone2 = models.CharField(max_length=100, null=False)
    dateofbirth = models.DateTimeField(null=True)
    nicnumber = models.CharField(max_length=100, null=False)
    profileimage = CloudinaryField('images', null=True, blank=True)
    nicimagefront = CloudinaryField('nic_images', null=True, blank=True)
    nicimageback = CloudinaryField('nic_images', null=True, blank=True)
    
    def __str__(self):
        return self.name
    