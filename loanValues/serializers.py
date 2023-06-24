import rest_framework.serializers as serializers
from .models import loanValue
from loans.models import Loan
from loans.serializers import loanSerializer


class loanValueSerializer(serializers.ModelSerializer):
    loan_number = serializers.SlugRelatedField(
        slug_field='loan_number',
        queryset=Loan.objects.all()
    )
    
    class Meta:
        model = loanValue
        fields = ( 'payment_date', 'payment_amout', 'interest', 'principle', 'balance' , 'loan_number')
        

        
        
