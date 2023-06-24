from django.db import models
from loans.models import Loan

# Create your models here.

class loanValue (models.Model):
    loan_number = models.ForeignKey(Loan, on_delete=models.SET_NULL , null=True , related_name='customer_loan_number' , db_column='loan_number')
    payment_date = models.DateField( null=False)
    payment_amout = models.FloatField( null=False )
    interest = models.FloatField( null=False )
    principle = models.FloatField( null=False )
    balance = models.FloatField( null=False )
    
    
    def __str__(self):
        return str(self.loan_number)