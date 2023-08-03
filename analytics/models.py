from django.db import models
from datetime import datetime
from  loanarrears.models import loanarrears
from CustomerProfile.models import CustomerProfile
from users.models import CustomUser
from loanvalues.models import loanValue
from loans.models import Loan
from dateutil.relativedelta import relativedelta
# Create your models here.


class analytics(models.Model):
    date_requested = models.CharField(max_length=100, null=True, blank=True)
    calculated_date = models.CharField(max_length=100 , null=True , blank=True)
    loan_count = models.IntegerField(null=True , blank=True)
    total_payments = models.FloatField(null=True , blank=True)
    total_loanArrears_accounts = models.IntegerField(null=True , blank=True)
    lastmonth_customer_count = models.IntegerField(null=True , blank=True)
    
    def __str__(self):
        return self.date_requested
    
    # def save(self, *args, **kwargs):
    #     last_month_date = datetime.now() - relativedelta(months=1)
    #     last_month_year = last_month_date.strftime("%Y-%m")
    #     current_date = datetime.now()
    #     self.calculated_date = last_month_year
    #     # Check if a record with the same last_month_year already exists
    #     existing_record = analytics.objects.filter(calculated_date=last_month_year).first()
    #     if existing_record:
    #         # If the record exists, update its values instead of creating a new one
    #         self.id = existing_record.id  # Set the ID to update the existing record
    #         self.loan_count = existing_record.loan_count
    #         self.total_payments = existing_record.total_payments
    #         self.total_loanArrears_accounts = existing_record.total_loanArrears_accounts
    #         self.lastmonth_customer_count = existing_record.lastmonth_customer_count
    #     else:
    #         # If the record doesn't exist, calculate and set the values
    #         total_value = 0
    #         loan_objects = Loan.objects.filter(loaned_date__contains=last_month_year)
    #         self.loan_count = loan_objects.count()
            
    #         payments = loanValue.objects.filter(payment_date__contains=last_month_year)
    #         for payment in payments:
    #             total_value += payment.payment_amount
    #         self.total_payments = total_value
            
    #         loanarrears_objects = loanarrears.objects.filter(arr_cal_date__contains=last_month_year).exclude(monthly_arrears=0)
    #         self.total_loanArrears_accounts = loanarrears_objects.count()
            
    #         user = CustomUser.objects.filter(date_joined__contains=last_month_year)
    #         monthly_customer = CustomerProfile.objects.filter(user_id__in=user)
    #         self.lastmonth_customer_count = monthly_customer.count()
        
    #     self.date_requested = current_date.strftime("%Y-%m-%d")
        
    #     super(analytics, self).save(*args, **kwargs)
        
        
    
    
    