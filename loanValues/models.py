from django.db import models
from loans.models import Loan
import numpy as np
from datetime import timedelta

# Create your models here.

class loanValue (models.Model):
    loan_number = models.ForeignKey(Loan, on_delete=models.SET_NULL , null=True , related_name='customer_loan_number' , db_column='loan_number')
    payment_date = models.DateField( null=False)
    payment_amout = models.FloatField( null=False )
    interest = models.FloatField( null=False )
    principle = models.FloatField( null=False )
    balance = models.FloatField( null=False )
    
    
    
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
            self.principle = np.round(self.payment_amout - self.interest , 2)
            self.balance = last_record.balance - self.principle
        else:
            daysfrompayment = (self.payment_date - self.loan_number.loaned_date).days
            self.interest = np.round(self.loan_number.loaned_amount * interestperday * daysfrompayment , 2)
            self.principle = np.round(self.payment_amout - self.interest , 2)
            self.balance = self.loan_number.loaned_amount - self.principle
         
        super(loanValue, self).save(*args, **kwargs)
        
        #TODO: maintaince balance with different loan accounts