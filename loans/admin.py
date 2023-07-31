from django.contrib import admin
from .models import Loan

class LoanAdmin(admin.ModelAdmin):
    search_fields = ['loan_number' , 'username']  # Add the field by which you want to search (loan_number in this case)

    # You can customize other attributes of the admin view if needed
    list_display = ['loan_number', 'username', 'loaned_date', 'branch_location', 'loaned_amount', 'bike_number', 'loan_period']
    list_filter = ['branch_location', 'loaned_date']
    ordering = ['-loaned_date', 'loan_number']
    # ... (other attributes as needed)

# Register the Loan model with the custom admin view
admin.site.register(Loan, LoanAdmin)
