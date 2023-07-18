from django.urls import path
from .views import GetStaffById

urlpatterns = [
    path('get/<int:id>' , GetStaffById.as_view() , name='getAllvalues')
]
