from rest_framework.serializers import ModelSerializer
from .models import Loan

class loanSerializer(ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'