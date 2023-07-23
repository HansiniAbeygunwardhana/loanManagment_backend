from .models import loanarrears
from django.db.models import Q

class loanarrearsuils:
    @classmethod
    def filter_by_assigned_location(cls , location):
            return loanarrears.filter_by_assigned_location(location)
        
    @classmethod
    def filter_by_loanaddress(cls , location):
            return loanarrears.filter_by_loanaddress(location)
        
    @classmethod
    def filter_by_location_and_price(cls ,location, pricemax, pricemin):
        queryset = loanarrears.objects.all()

        if location:
            queryset = queryset.filter(loan_id__username__address__icontains=location)

        if pricemax:
            queryset = queryset.filter(monthly_arrears__lte=pricemax)

        if pricemin:
            queryset = queryset.filter(monthly_arrears__gt=pricemin)
            
        queryset = queryset.values('loanarrears_id').distinct()

        return queryset