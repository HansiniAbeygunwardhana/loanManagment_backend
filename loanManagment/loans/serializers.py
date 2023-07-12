from rest_framework import  serializers	
from .models import Loan
from CustomerProfile.models import CustomUser as User
from CustomerProfile.serializers import CustomerNameIDSerializer

class loanSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Loan
        fields = '__all__'
        

class simpleLoanSerializer(serializers.ModelSerializer):
    
    username = CustomerNameIDSerializer()
    
    loaned_amount = serializers.SerializerMethodField()
    loan_id = serializers.SerializerMethodField()
    
    def get_loaned_amount(self, obj):
        return str(obj.loaned_amount)
    
    def get_loan_id(self, obj):
        return str(obj.loan_id)
    
    class Meta:
        model = Loan
        fields = [ 'loan_id','username', 'loaned_date', 'branch_location', 'loaned_amount' , 'loan_number'	]
        
        
        
class loanNumbererializer(serializers.ModelSerializer):
    
    username = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    
    class Meta:
        model = Loan
        fields = [ 'loan_id','username', 'loaned_amount' , 'loan_number']
        
        
class loanIDandNumberSerializer(serializers.ModelSerializer):
    
    username = CustomerNameIDSerializer()
    
    class Meta:
        model = Loan
        fields = [ 'loan_id','username', 'loan_number']