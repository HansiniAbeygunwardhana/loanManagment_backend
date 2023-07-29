from django.urls import path
from .views import AddArrears , GetArrears , FilterLoanArrearsbyStaff , AddAllLoanArrears , ListLoanArrearsByLocation , FilterLoanArrears , LoanArrearsListView 
from .views import  LoanArrearsListView
# http://127.0.0.1:8000/arrears/......

urlpatterns = [
    path('add' , AddArrears.as_view() , name='addarrears'),
    path('getbyloanid/<int:loan_id>' , GetArrears.as_view() , name='getarrears'),
    path('getall/' , FilterLoanArrears.as_view() , name='getarrearsbyloanid'),
    path('getallbyid/' , LoanArrearsListView.as_view() , name='getarrearsbyloanid'),
    path('calall' , AddAllLoanArrears.as_view() , name='Add All arrears'),
    path('getbylocation/' , ListLoanArrearsByLocation.as_view() , name='getarrearsbylocation'),
    path('getbystaff/' , FilterLoanArrearsbyStaff.as_view() , name='FilterLoanArrearsbyStaff')
    
]
