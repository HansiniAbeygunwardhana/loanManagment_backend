from loanvalues.views import getAllLoans , LoanValueCreateView , getLoanValues
from django.urls import path

# http://127.0.0.1:8000/loanvalues/.........

urlpatterns = [
   path('all/<int:loan_number>' , getLoanValues , name='getLoanValues'),
   path('update/' , LoanValueCreateView.as_view() , name='updateLoanValues'),
   path('' , getAllLoans.as_view() , name='getAllvalues')
]