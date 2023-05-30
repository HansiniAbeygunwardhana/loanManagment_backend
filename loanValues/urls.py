from . import views
from django.urls import path

urlpatterns = [
    path('loanvalues', views.calLoanValues, name='loanValues')
]
