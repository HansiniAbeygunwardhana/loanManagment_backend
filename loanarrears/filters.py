from django_filters import rest_framework as filters
from .models import loanarrears

class LoanArrearsFilter(filters.filterset):
    loan_id = filters.NumberFilter(field_name='loan_id' , distinct=True)
    
    class Meta:
        model = loanarrears
        fields = ['loan_id']