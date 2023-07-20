from django.urls import path
from .views import GetStaffById ,  AddStaff

urlpatterns = [
    path('get/<int:id>' , GetStaffById.as_view() , name='getAllvalues'),
    path('add/' , AddStaff.as_view() , name='addstaff')
]
