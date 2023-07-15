from django.contrib import admin
from loanvalues.models import loanValue

# Register your models here.
class loanValueAdmin(admin.ModelAdmin):
    list_display = ('loan_number', 'payment_date', 'payment_amount')
    readonly_fields = ('interest', 'principle', 'balance' , 'interest_paid_date')
    fields = ('loan_number', 'payment_date', 'payment_amount', 'interest', 'principle', 'balance' , 'interest_paid_date')

admin.site.register(loanValue, loanValueAdmin)