from django.db import models
from users.models import User

# Create your models here.

class Manager (User):
    
    branchLocation = (
        ('Polonnaruwa', 'Polonnaruwa'),
        ('Hingurakgoda', 'Hingurakgoda'),
        ('Diyasenpura', 'Diyasenpura'),
        ('Sewanapitiya', 'Sewanapitiya'),
        ('Dehiaththakandiya', 'Dehiaththakandiya'),
        ('Mahiyanganaya', 'Mahiyanganaya'),
    )
    

    name = models.CharField(max_length=100, null=False, unique=True)
    surname = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    telephone1 = models.CharField(max_length=100, null=False)
    telephone2 = models.CharField(max_length=100, null=False)
    dateofbirth = models.DateField(null=True)
    nicnumber = models.CharField(max_length=100, null=False)
    branch = models.CharField(max_length=20 , choices=branchLocation , default='Sewanapitiya')
    
    def __str__(self):
        return self.name