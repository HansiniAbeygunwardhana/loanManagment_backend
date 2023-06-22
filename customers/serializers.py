from .models import Customer
from rest_framework.serializers import ModelSerializer

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name','address',  'email', 'telephone1', 'telephone2', 'nicnumber', 'surname']
        
        