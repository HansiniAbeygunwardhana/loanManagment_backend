from django.db import models
from users.models import User
from django.conf import settings

# Create your models here.
class Loan(models.Model):
    
    branches = (
        ('polonnaruwa' , 'Polonnaruwa'),
        ('diyasenpura' , 'Diyasenpura'),
        ('sewanapitiya' , 'Sewanapitiya'),
        ('dehiaththakandiya' , 'Dehiaththakandiya'),
        ('mahiyanaganaya' , 'Mahiyanaganaya'),
        )
    
    loan_id = models.IntegerField(primary_key=True)
    loan_name = models.CharField(max_length=100)
    branch_location = models.CharField(max_length=20, choices=branches)
    loan_amount = models.FloatField()
    username = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    bike_number = models.CharField(max_length=12)
    first_guarantor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='first_guarantor', null=True)
    second_guarantor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='second_guarantor', null=True)
    

    def __str__(self):
        return self.loan_name