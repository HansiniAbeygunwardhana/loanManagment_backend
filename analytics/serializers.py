from rest_framework import serializers
from .models import analytics


class AanalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = analytics
        fields = '__all__'
        
        
class AnalyticsTotalCustomers(serializers.ModelSerializer):
    class Meta:
        model = analytics
        fields = ('lastmonth_customer_count' , 'calculated_date')
        
class AnalyticsTotalLoans(serializers.ModelSerializer):
    class Meta:
        model = analytics
        fields = ('loan_count' , 'calculated_date')
        
class AnalyticsTotalPayments(serializers.ModelSerializer):
    class Meta:
        model = analytics
        fields = ('total_payments' , 'calculated_date')
        
class AnalyticsTotalArrears(serializers.ModelSerializer):
    class Meta:
        model = analytics
        fields = ('total_loanArrears_accounts' , 'calculated_date')