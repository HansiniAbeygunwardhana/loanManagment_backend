from rest_framework.serializers import ModelSerializer
from .models import Loans

class loanSerializer(ModelSerializer):
    class Meta:
        model = Loans
        fields = '__all__'