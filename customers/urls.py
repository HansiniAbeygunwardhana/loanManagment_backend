from . import views
from django.urls import path

urlpatterns = [
    path('getcustomers/', views.getCustomers, name='getCustomers'),
    path('addcustomers/', views.addCustomers, name='addCustomers'),
]