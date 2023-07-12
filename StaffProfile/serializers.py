from rest_framework import serializers
from .models import StaffProfile
from users.serializers import UserSerializer

class StaffProfileSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    
    class Meta:
        model = StaffProfile
        fields = '__all__'
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        staff_profile = StaffProfile.objects.create(user=user, **validated_data)
        return staff_profile
        
    
    
        
    