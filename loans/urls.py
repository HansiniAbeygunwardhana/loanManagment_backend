from . import views
from django.urls import path

urlpatterns = [
    path('getloans', views.getLoans, name='getloans'),
    path('addloans', views.addLoans, name='addloans'),
    path('getloans/<int:loan_id>', views.getMoreLoanDetails, name='getloan')
]
