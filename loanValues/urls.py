from loanValues.views import getAllLoans , LoanValueCreateView , getLoanValues
from django.urls import path

urlpatterns = [
   path('all/<int:loan_number>' , getLoanValues , name='getLoanValues'),
   path('update/' , LoanValueCreateView.as_view() , name='updateLoanValues'),
   path('' , getAllLoans.as_view() , name='getAllvalues')
]
