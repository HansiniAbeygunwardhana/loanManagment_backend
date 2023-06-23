from django.db import models
from users.models import User
from django.conf import settings

# Create your models here.
class Loan(models.Model):
    
    branches = (
        ('Polonnaruwa' , 'Polonnaruwa'),
        ('Diyasenpura' , 'Diyasenpura'),
        ('Sewanapitiya' , 'Sewanapitiya'),
        ('Dehiaththakandiya' , 'Dehiaththakandiya'),
        ('Mahiyanaganaya' , 'Mahiyanaganaya'),
        )
    
    loan_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    loaned_date = models.DateField( default='2020-01-01' , null=False)
    branch_location = models.CharField(max_length=20, choices=branches)
    loaned_amount = models.FloatField(null=False)
    bike_number = models.CharField(max_length=12)
    first_guarantor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='first_guarantor', null=True)
    second_guarantor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='second_guarantor', null=True)
    
