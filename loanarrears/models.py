from django.utils import timezone
from django.db import models
from loans.models import Loan
from  StaffProfile.models import StaffProfile
from loanvalues.models import loanValue
import numpy_financial as npf
import numpy as np
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.core.exceptions import ValidationError


# Create your models here.
class loanarrears(models.Model):
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE , related_name='loanarrears')
    monthly_payment = models.FloatField()
    monthly_arrears = models.FloatField()
    arr_cal_date = models.DateField( null=False , default=timezone.now)
    staff = models.ForeignKey(StaffProfile, on_delete=models.DO_NOTHING , related_name='loanarrears' , default=4)
    loan_values = models.ForeignKey(loanValue, on_delete=models.SET_NULL , related_name='loanarrears' , null=True)
    additional_fees = models.FloatField( null=False , default=0 )
    
    
    def save(self, *args, **kwargs):
        
        MAX_RECORDS_PER_LOAN = 3
        
        # Check if a staff was previously assigned to this loan ID
        if self.loan_id:
            last_loanarrears = loanarrears.objects.filter(loan_id=self.loan_id).order_by('-id').first()
            if last_loanarrears:
                self.staff = last_loanarrears.staff
            else :
                self.staff = StaffProfile.objects.get(id=1)
            
                
                  
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

        # Check if this loan ID already has 5 records
        existing_records_count = loanarrears.objects.filter(loan_id=self.loan_id).count()
        if existing_records_count >= MAX_RECORDS_PER_LOAN:
            # Delete the oldest record
            oldest_record = loanarrears.objects.filter(loan_id=self.loan_id).order_by('id').first()
            oldest_record.delete()

        super(loanarrears, self).save(*args, **kwargs)
        
        
    def calculate_shallhavebalance (self , arr_months , loanamount , interestrate , loanperiod):
        
        total_principle = 0
        for arr_month in range(arr_months):
            principle = np.round(npf.ppmt(interestrate/12/100 , arr_month+1 , loanperiod , -loanamount ) , 2)
            total_principle += principle
        
        return loanamount - total_principle
    
    def clean(self):
        # Check if monthly_arrears is 0, and if so, prevent saving the model
        if self.monthly_arrears == 0:
            raise ValidationError("Monthly arrears must be greater than 0 to save the model.")
    
    @classmethod
    def filter_by_assigned_location(cls, location):
        return cls.objects.filter(staff__assigned_location=location)
    
    @classmethod
    def filter_by_loanaddress(cls , location):
        return cls.objects.filter(loan_id__username__address__icontains=location)
    
    @classmethod
    def filter_by_location_and_price(cls , location , pricemax , pricemin):
        return cls.objects.filter(Q(loan_id__username__address__icontains=location) & Q(loan_id__loaned_amount__lte=pricemax) & Q(loan_id__loaned_amount__gt=pricemin))
    
    
    
    
    