from rest_framework import  serializers	
from .models import Loan
from CustomerProfile.models import CustomUser as User
from CustomerProfile.serializers import CustomerNameIDSerializer , CustomerProfileOnlySerializer , CustomerProfileOnlySerializerWithId
from CustomerProfile.models import CustomerProfile
class CustomerProfileOnlySerializerForLoan(serializers.ModelSerializer):
    
   
    email = serializers.EmailField(source='user.email')
    
    class Meta:
        model = CustomerProfile
        fields = ['name' , 'surname' , 'address' , 'telephone1' , 'telephone2' , 'dateofbirth' , 'nicnumber' ,  'email' , 'id'	, 'user']


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
    
    class Meta:
        model = Loan
        fields = [ 'loan_id','username', 'loaned_amount' , 'loan_number']
        
        
class loanIDandNumberSerializer(serializers.ModelSerializer):
    
    username = CustomerNameIDSerializer()
    
    class Meta:
        model = Loan
        fields = [ 'loan_id','username', 'loan_number']
        
class loanSerializerExtended(serializers.ModelSerializer):
        
    username = CustomerProfileOnlySerializerForLoan()
    first_guarantor = CustomerProfileOnlySerializerForLoan()
    second_guarantor = CustomerProfileOnlySerializerForLoan()
    
    class Meta:
        model = Loan
        fields = '__all__'
        
class loanSerializerCustomerIds(serializers.ModelSerializer):
    
    userId = serializers.IntegerField(source='username.id')
    
    class Meta:
        model = Loan
        fields = [ 'userId', 'loan_number']
        
        
class loanSerializerCustomerId(serializers.ModelSerializer):
    
    username = serializers.CharField(source='username.username')
    first_guarantor = serializers.CharField(source='first_guarantor.username')
    second_guarantor = serializers.CharField(source='second_guarantor.username')
    
    class Meta:
        model = Loan
        fields = '__all__'
        
        