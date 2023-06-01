from .models import customer
from users.models import User
from rest_framework.serializers import ModelSerializer

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'
        
        
class userSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'user_type']