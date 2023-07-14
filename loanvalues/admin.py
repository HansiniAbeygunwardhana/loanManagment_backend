from django.contrib import admin
from loanvalues.models import loanValue

# Register your models here.
class loanValueAdmin(admin.ModelAdmin):
    list_display = ('loan_number', 'payment_date', 'payment_amount')
    readonly_fields = ('interest', 'principle', 'balance')
    fields = ('loan_number', 'payment_date', 'payment_amount', 'interest', 'principle', 'balance')

admin.site.register(loanValue, loanValueAdmin)