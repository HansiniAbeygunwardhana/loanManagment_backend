from django.urls import path
from .views import UserViewSet , MyTokenObtainPairView
from StaffProfile.views import ListStaff , AddStaff
from CustomerProfile.views import ListCustomer , AddCustomer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

## http://127.0.0.1:8000/users/..................

urlpatterns = [
    
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('' , UserViewSet.as_view() , name='user' ),
    path('staff/' , ListStaff.as_view() , name='staff' ),
    path('staff/add' , AddStaff.as_view() , name='add_staff' ),
    path('customer/' , ListCustomer.as_view() , name='customer' ),
    path('customer/add' , AddCustomer.as_view() , name='add_customer' ),
]