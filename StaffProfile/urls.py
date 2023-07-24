from django.urls import path
from .views import GetStaffById ,  AddStaff

# http://127.0.0.1:8000/staff/.....


urlpatterns = [
    path('get/<int:id>' , GetStaffById.as_view() , name='getAllvalues'),
    path('add/' , AddStaff.as_view() , name='addstaff')
]
