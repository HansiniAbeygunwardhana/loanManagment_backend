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
    date_requested = models.DateField( null=True , default=datetime.now),
    calculated_date = models.CharField(max_length=100 , null=True , blank=True)
    loan_count = models.IntegerField(null=True , blank=True)
    total_payments = models.FloatField(null=True , blank=True)
    total_loanArrears_accounts = models.IntegerField(null=True , blank=True)
    monthly_customer_count = models.IntegerField(null=True , blank=True)
    
    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        self.date = datetime.now()
        total_value = 0
        last_month_date = datetime.now() - relativedelta(months=1)
        last_month_year = last_month_date.strftime("%Y-%m")
        self.calculated_date = last_month_year
        current_year_month = self.date.strftime("%Y-%m")
        
        loan_objects = Loan.objects.filter(loaned_date__contains=current_year_month)
        self.loan_count = loan_objects.count()
        
        payments = loanValue.objects.filter(payment_date__contains=current_year_month)
        for payment in payments:
            total_value += payment.payment_amount
        self.total_payments = total_value
        
        loanarrears_objects = loanarrears.objects.filter(arr_cal_date__contains=current_year_month).exclude(monthly_arrears=0)
        self.total_loanArrears_accounts = loanarrears_objects.count()
        
        user = CustomUser.objects.filter(date_joined__contains=current_year_month)
        monthly_customer = CustomerProfile.objects.filter(user_id__in=user)
        self.monthly_customer_count = monthly_customer.count()
        
        print(loan_objects.count())
        
        super(analytics, self).save(*args, **kwargs)
        
    
    
    