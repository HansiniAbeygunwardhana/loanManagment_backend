from django.db import models
from loans.models import Loan

# Create your models here.

class loanValue (models.Model):
    loan_id = models.ForeignKey(Loan, on_delete=models.SET_NULL , null=True , related_name='customer_loan_id' , db_column='loan_id')
    loan_amount = models.ForeignKey(Loan, on_delete=models.SET_NULL , null=True , related_name='customer_loan_amount' , db_column='loan_amount')
    payment_date = models.DateField( null=False)
    payment_amout = models.FloatField( null=False )
    interest = models.FloatField( null=False )
    principle = models.FloatField( null=False )
    balance = models.FloatField( null=False )
    
    def save(self, *args, **kwargs):
        self.balance = self.loan_amount - self.principle  # Update the balance field
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.loan_id)