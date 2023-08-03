from django.contrib import admin
from .models import Loan


class LoanAdmin(admin.ModelAdmin):
    search_fields = ['loan_number' , 'username']
    list_display = ['loan_number', 'username', 'loaned_date', 'branch_location', 'loaned_amount', 'bike_number', 'loan_period']
    list_filter = ['branch_location', 'loaned_date']
    ordering = ['-loaned_date', 'loan_number']
admin.site.register(Loan, LoanAdmin)



