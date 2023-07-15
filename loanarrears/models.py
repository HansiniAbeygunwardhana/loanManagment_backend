from django.utils import timezone
from django.db import models
from loans.models import Loan
from  StaffProfile.models import StaffProfile
from loanvalues.models import loanValue
import numpy_financial as npf
import numpy as np
from dateutil.relativedelta import relativedelta

# Create your models here.
class loanarrears(models.Model):
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE , related_name='loanarrears')
    monthly_payment = models.FloatField()
    monthly_arrears = models.FloatField()
    arr_cal_date = models.DateField( null=False , default=timezone.now)
    staff = models.ForeignKey(StaffProfile, on_delete=models.DO_NOTHING , related_name='loanarrears' , null=True)
    loan_values = models.ForeignKey(loanValue, on_delete=models.DO_NOTHING , related_name='loanarrears')
    additional_fees = models.FloatField( null=True )
    
    
    def save(self, *args, **kwargs):
        
        last_loanarrears = loanarrears.objects.filter(loan_id=self.loan_id).order_by('-id').first()
        if last_loanarrears:
            self.staff = StaffProfile.objects.get(staff_id=self.staff.id)
            self.additional_fees += last_loanarrears.additional_fees
            
        interestrate = 42.0
        arr_months = relativedelta(self.arr_cal_date , self.loan_id.loaned_date).months
        loanRecord = Loan.objects.get(loan_id=self.loan_id.loan_id)
        self.monthly_payment = np.round(npf.pmt(interestrate/100/12 , loanRecord.loan_period , -loanRecord.loaned_amount) , 2)
        should_have_balance = self.calculate_shallhavebalance(arr_months , loanRecord.loaned_amount , interestrate , loanRecord.loan_period)
        last_loan_value = loanValue.objects.filter(loan_number=self.loan_id.loan_id).order_by('-id').first()
        self.loan_values = last_loan_value
        
        if last_loan_value:
            if self.loan_values.balance < should_have_balance:
                self.monthly_arrears = 0
            else :
                self.loan_values = last_loan_value
                not_paid_interest =  (self.arr_cal_date - last_loan_value.interest_paid_date).days * last_loan_value.balance * interestrate / 365 / 100
                self.monthly_arrears = np.round(last_loan_value.balance + not_paid_interest - should_have_balance , 2)
        else:
            if self.loan_id.loaned_amount < should_have_balance:
                self.monthly_arrears = 0
            else:
                not_paid_interest = (self.arr_cal_date - self.loan_id.loaned_date).days * loanRecord.loaned_amount * interestrate / 365 / 100
                self.monthly_arrears = np.round(loanRecord.loaned_amount + not_paid_interest - should_have_balance , 2)

        super(loanarrears, self).save(*args, **kwargs)
        
        
    def calculate_shallhavebalance (self , arr_months , loanamount , interestrate , loanperiod):
        
        total_principle = 0
        for arr_month in range(arr_months):
            principle = np.round(npf.ppmt(interestrate/12/100 , arr_month+1 , loanperiod , -loanamount ) , 2)
            total_principle += principle
        
        return loanamount - total_principle
    
    
    
    