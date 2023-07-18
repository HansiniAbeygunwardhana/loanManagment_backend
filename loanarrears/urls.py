from django.urls import path
from .views import AddArrears , GetArrears , LoanArrearsList , AddAllLoanArrears

# http://127.0.0.1:8000/arrears/......

urlpatterns = [
    path('add' , AddArrears.as_view() , name='addarrears'),
    path('getbyloanid/<int:loan_id>' , GetArrears.as_view() , name='getarrears'),
    path('getall/' , LoanArrearsList.as_view() , name='getarrearsbyloanid'),
    path('calall' , AddAllLoanArrears.as_view() , name='Add All arrears'),
]
