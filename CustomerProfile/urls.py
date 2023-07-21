from django.urls import path
from .views import ListCustomerNames , GetOneCustomer

# http://127.0.0.1:8000/customers/..................

urlpatterns = [
    path('getnames' , ListCustomerNames.as_view() , name='user' ),
    path('getone/<int:id>/' , GetOneCustomer.as_view() , name='user')
]

