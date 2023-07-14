from django.db import models
from loans.models import Loan
import numpy as np
from datetime import datetime

# Create your models here.

class loanValue (models.Model):
    loan_number = models.ForeignKey(Loan, on_delete=models.DO_NOTHING , null=True , related_name='customer_loan_number' , db_column='loan_number')
    payment_date = models.DateField( null=False)
    payment_amount = models.FloatField( null=False )
    interest = models.FloatField( null=True )
    principle = models.FloatField( null=True )
    balance = models.FloatField( null=True )
    interest_paid_date = models.DateField( null=True)
    
    
    
    ## Daily interest rate = 0.00115068
    def __str__(self):
        return str(self.balance) 
    
    def save(self, *args, **kwargs):
        
        interestrate = 42.0
        interestperday = interestrate /365/100
        
        
        last_record = loanValue.objects.filter(loan_number=self.loan_number).order_by('-id').first()
        if last_record:
            daysfrompayment = (self.payment_date - last_record.payment_date).days
            self.interest = np.round(last_record.balance * interestperday * daysfrompayment , 2)
            self.principle = np.round(self.payment_amount - self.interest , 2)
            self.balance = np.round(last_record.balance - self.principle , 3)
        else:
            daysfrompayment = (self.payment_date - self.loan_number.loaned_date).days
            self.interest_paid_date = datetime.now().date() - self.loan_number.loaned_date.date()
            self.interest = np.round(self.loan_number.loaned_amount * interestperday * daysfrompayment , 2)
            self.principle = np.round(self.payment_amount - self.interest , 2)
            self.balance = np.round(self.loan_number.loaned_amount - self.principle , 3)
         
        super(loanValue, self).save(*args, **kwargs)
        