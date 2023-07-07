from .views import getLoans, addLoans, getMoreLoanDetails, getAllLoanNumbers ,getAllLoans
from django.urls import path

urlpatterns = [
    path('getloans', getLoans, name='getloans'),
    path('addloans', addLoans, name='addloans'),
    path('getloans/<int:loan_id>', getMoreLoanDetails, name='getloan'),
    path('allnumbers', getAllLoans.as_view(), name='getallnumbers'),
]
