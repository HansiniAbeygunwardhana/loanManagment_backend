from django.urls import path
from .views import ListCustomerNames


urlpatterns = [
    path('getnames' , ListCustomerNames.as_view() , name='user' ),
]

