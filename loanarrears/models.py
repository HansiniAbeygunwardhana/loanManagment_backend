from django.utils import timezone
from django.db import models
from loans.models import Loan
from  StaffProfile.models import StaffProfile
from loanvalues.models import loanValue
import numpy_financial as npf
import numpy as np

# Create your models here.
class loanarrears(models.Model):
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE , related_name='loanarrears')
    monthly_payment = models.FloatField()
    monthly_arrears = models.FloatField()
    arr_cal_date = models.DateField( null=False , default=timezone.now)
    staff = models.ForeignKey(StaffProfile, on_delete=models.DO_NOTHING , related_name='loanarrears')
    loan_values = models.ForeignKey(loanValue, on_delete=models.DO_NOTHING , related_name='loanarrears')
    
    
    def save(self, *args, **kwargs):
        
        interestrate = 42.0
        
        loanRecord = Loan.objects.get(loan_id=self.loan_id.loan_id)
        last_loan_value = loanValue.objects.filter(loan_number=self.loan_id.loan_id).order_by('-id').first()
       
        if loanRecord:
            if last_loan_value:
                self.loan_values = loanValue.objects.create(loan_number=self.loan_id.loan_id , loan_value=loanRecord.loaned_amount)
                self.monthly_payment = np.round(npf.pmt(interestrate/100/12 , loanRecord.loan_period , -loanRecord.loaned_amount) , 2)
                not_paid_interest_dates = last_loan_value.payment_date - loanRecord.loaned_date 
                
        else :
            self.monthly_payment = 0
            
        self.monthly_arrears = 0

        super(loanarrears, self).save(*args, **kwargs)
    
    
    