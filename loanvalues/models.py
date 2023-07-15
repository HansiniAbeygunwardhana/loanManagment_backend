from django.db import models
from loans.models import Loan
import numpy as np
from datetime import date , timedelta

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
            tobepaid_days = self.payment_date - last_record.interest_paid_date
            if self.payment_amount > tobepaid_days.days * last_record.balance * interestperday:
                self.interest = np.round(tobepaid_days.days * last_record.balance * interestperday , 2)
                self.principle = np.round(self.payment_amount - self.interest , 2)
                self.balance = last_record.balance - self.principle
                self.interest_paid_date = last_record.interest_paid_date + tobepaid_days
            else:
                canbepaid_days = int(self.payment_amount / (last_record.balance * interestperday))
                self.interest_paid_date = last_record.interest_paid_date + timedelta(days=canbepaid_days)
                self.balance = last_record.balance
                self.principle = 0
                self.interest = self.payment_amount
        else:
            tobepaid_days = self.payment_date - self.loan_number.loaned_date
            if self.payment_amount > tobepaid_days.days * self.loan_number.loaned_amount * interestperday:
                self.interest = np.round(tobepaid_days.days * self.loan_number.loaned_amount * interestperday , 2)
                self.principle = np.round(self.payment_amount - self.interest , 2)
                self.balance = self.loan_number.loaned_amount - self.principle
                self.interest_paid_date = self.loan_number.loaned_date + tobepaid_days
            else:
                canbepaid_days = int(self.payment_amount / (self.loan_number.loaned_amount * interestperday))
                self.interest_paid_date = self.loan_number.loaned_date + timedelta(days=canbepaid_days)
                self.balance = self.loan_number.loaned_amount
                self.principle = 0
                self.interest = self.payment_amount
            
         
        super(loanValue, self).save(*args, **kwargs)
        