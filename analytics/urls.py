from django.urls import path
from .views import UpdateAnalytics , AnalyticsTotalArrearsView , AnalyticsTotalCustomersView , AnalyticsTotalLoansView , AnalyticsTotalPaymentsView

urlpatterns = [
    path('' , UpdateAnalytics.as_view() , name='updateanalytics'),
    path('customers/' , AnalyticsTotalCustomersView.as_view() , name='totalcustomers'),
    path('loans/' , AnalyticsTotalLoansView.as_view() , name='totalloans'),
    path('payments/' , AnalyticsTotalPaymentsView.as_view() , name='totalpayments'),
    path('arrears/' , AnalyticsTotalArrearsView.as_view() , name='totalarrears'),
]
