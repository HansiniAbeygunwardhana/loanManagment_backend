from rest_framework import serializers
from .models import loanarrears

class loanArrearsSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = loanarrears
        fields = ['loan_id', 'staff', 'arr_cal_date' , 'additional_fees']
        
class loanArrearsSerializer(serializers.ModelSerializer):
    
    loan_id = serializers.CharField(source='loan_id.loan_number')
    
    class Meta:
        model = loanarrears
        fields = '__all__'
        
class ArrearsCardSerializer(serializers.ModelSerializer):
    
    loan_id = serializers.CharField(source='loan_id.loan_number')
    customer_name = serializers.CharField(source='loan_id.username.name')
    customer_addess = serializers.CharField(source='loan_id.username.address')
    customer_telephone = serializers.CharField(source='loan_id.username.telephone1')
    
     
    class Meta:
        model = loanarrears
        fields = ['loan_id' , 'monthly_arrears' , 'monthly_payment' , 'arr_cal_date' , 'customer_name' , 'customer_addess' , 'customer_telephone' , 'id']