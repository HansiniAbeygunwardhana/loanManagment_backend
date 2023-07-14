from django.contrib import admin
from .models import loanarrears

# Register your models here.
class loanArrears(admin.ModelAdmin):
    list_display = ('loan_id', 'loan_values', 'staff' )
    readonly_fields = ('monthly_arrears', 'loan_values' , 'monthly_payment')
    fields = ('loan_id', 'monthly_payment', 'monthly_arrears', 'staff', 'loan_values')
    
admin.site.register(loanarrears, loanArrears)