from django.urls import path
from .views import AddArrears

urlpatterns = [
    path('add' , AddArrears.as_view() , name='addarrears')
]
