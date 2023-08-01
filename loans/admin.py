from django.contrib import admin
from .models import Loan

def mark_as_pending(modeladmin, request, queryset):
    queryset.update(pending=True)
    
mark_as_pending.short_description = "Mark selected loans as pending"

class LoanAdmin(admin.ModelAdmin):
    search_fields = ['loan_number' , 'username']
    list_display = ['loan_number', 'username', 'loaned_date', 'branch_location', 'loaned_amount', 'bike_number', 'loan_period']
    list_filter = ['branch_location', 'loaned_date']
    ordering = ['-loaned_date', 'loan_number']
    actions = [mark_as_pending]
admin.site.register(Loan, LoanAdmin)



