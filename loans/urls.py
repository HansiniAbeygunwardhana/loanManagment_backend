from . import views
from django.urls import path

urlpatterns = [
    path('getloans', views.getLoans, name='getloans'),
]
