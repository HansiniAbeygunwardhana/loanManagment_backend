from django.urls import path
from .views import UpdateAnalytics

urlpatterns = [
    path('' , UpdateAnalytics.as_view() , name='updateanalytics'),
]
