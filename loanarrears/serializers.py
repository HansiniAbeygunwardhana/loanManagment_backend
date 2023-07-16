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