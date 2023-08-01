from django.contrib import admin
from .models import analytics
# Register your models here.


class Analyticsadmin(admin.ModelAdmin):
    readonly_fields = ( 'date_requested' ,'calculated_date' , 'loan_count' , 'total_payments' , 'total_loanArrears_accounts' , 'lastmonth_customer_count')
    fields = ('date_requested' , 'calculated_date' , 'loan_count' , 'total_payments' , 'total_loanArrears_accounts' , 'lastmonth_customer_count')


admin.site.register(analytics , Analyticsadmin)