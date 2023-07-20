from rest_framework import serializers
from .models import CustomerProfile
from users.serializers import UserSerializer

class CustomerProfileSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    
    class Meta:
        model = CustomerProfile
        fields = '__all__'
        
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
    
    class Meta:
        model = CustomerProfile
        fields = '__all__'