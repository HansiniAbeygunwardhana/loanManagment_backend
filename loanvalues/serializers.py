import rest_framework.serializers as serializers
from .models import loanValue
from loans.models import Loan
from loans.serializers import loanSerializer , loanIDandNumberSerializer 


class loanValueSerializer(serializers.ModelSerializer):
    loan_number = serializers.SlugRelatedField(
        slug_field='loan_number' ,
        queryset=Loan.objects.all()
    )
    
    class Meta:
        model = loanValue
        fields =[ 'payment_date' , 'payment_amount' , 'loan_number' , 'interest' , 'principle' , 'balance' , 'id']
        

class loanValueSerializer2(serializers.ModelSerializer):
    
    loan_number = loanIDandNumberSerializer()
    
    class Meta:
        model = loanValue
        fields =[ 'payment_date' , 'payment_amount' , 'loan_number']
 
        
class LoanValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = loanValue
        fields = ['payment_date', 'payment_amount', 'loan_number']
        