from django.urls import path
from .views import GetStaffById ,  AddStaff , GetStaffHome

# http://127.0.0.1:8000/staff/.....


urlpatterns = [
    path('get/<int:id>' , GetStaffById.as_view() , name='getAllvalues'),
    path('add/' , AddStaff.as_view() , name='addstaff'),
    path('getbyid/<int:id>' , GetStaffHome.as_view() , name='addstaff'),
]
