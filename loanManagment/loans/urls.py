from django.urls import path
from .views import getLoans, addLoans, getMoreLoanDetails, getAllLoanNumbers ,getAllLoans

# http://127.0.0.1:8000/loans/...............

urlpatterns = [
    path('getall', getLoans, name='getloans'),
    path('add', addLoans, name='addloans'),
    path('get/<int:loan_id>', getMoreLoanDetails, name='getloan'),
    path('allnumbers', getAllLoans.as_view(), name='getallnumbers'),
]
