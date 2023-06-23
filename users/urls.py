from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenRefreshView)
from .views import MyTokenObtainPairView

urlpatterns = [
    path('token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('customer', views.customer_registration, name='customer_registration'),
    path('manager', views.manager_registration, name='manager_registration'),
    path('staff', views.staff_registration, name='staff_registration'),
    path('viewcustomer', views.getCustomers, name='get_customers'),
]