from rest_framework import serializers
from .models import StaffProfile
from users.serializers import UserSerializer

class StaffProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')
    usertype = serializers.CharField(source='user.usertype')
    is_collector = serializers.BooleanField(source='user.is_collector')

    class Meta:
        model = StaffProfile
        fields = ['username', 'email', 'password', 'usertype', 'name', 'surname', 'address', 'telephone1', 'telephone2', 'dateofbirth', 'nicnumber', 'branch', 'is_collector']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        staff_profile = StaffProfile.objects.create(user=user, **validated_data)
        return staff_profile

    
    
class StaffSerializerByName(serializers.ModelSerializer):
        
        class Meta:
            model = StaffProfile
            fields = ['name' , 'assigned_location' , 'id']
        
    
    
        
    