from .views import getLoanValues
from django.urls import path

urlpatterns = [
   path('all/<int:loan_number>' , getLoanValues , name='getLoanValues'),
]
