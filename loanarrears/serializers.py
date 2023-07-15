from rest_framework.serializers import ModelSerializer
from .models import loanarrears

class loanArrearsSerializerBasic(ModelSerializer):
    class Meta:
        model = loanarrears
        fields = ['loan_id', 'staff', 'arr_cal_date']
        
class loanArrearsSerializer(ModelSerializer):
    class Meta:
        model = loanarrears
        fields = '__all__'