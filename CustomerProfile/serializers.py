from rest_framework import serializers
from .models import CustomerProfile
from users.serializers import UserSerializer

class CustomerProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')
    usertype = serializers.CharField(source='user.usertype')

    class Meta:
        model = CustomerProfile
        fields = ['username', 'email', 'password', 'usertype', 'name', 'surname', 'address', 'telephone1', 'telephone2', 'dateofbirth', 'nicnumber', 'profileimage']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        customer_profile = CustomerProfile.objects.create(user=user, **validated_data)
        return customer_profile

class CustomerNameIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerProfile
        fields = ['name' , 'id']
               
class CustomerProfileOnlySerializer(serializers.ModelSerializer):
    
    profileimage = serializers.ImageField(max_length=None, use_url=True)
    email = serializers.EmailField(source='user.email')
    
    class Meta:
        model = CustomerProfile
        fields = ['name' , 'surname' , 'address' , 'telephone1' , 'telephone2' , 'dateofbirth' , 'nicnumber' , 'profileimage' , 'email'	]
        
class CustomerImageOnlySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerProfile
        fields = ['profileimage']
        
        
class HomeScreenCustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerProfile
        fields = ['name' , 'surname' , 'profileimage' , 'address' ]
        
class BasicCustomerData(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerProfile
        fields = ['name' , 'address' , 'telephone1' , 'nicnumber' ]
