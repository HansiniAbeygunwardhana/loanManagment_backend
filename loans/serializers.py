from rest_framework import  serializers	
from .models import Loan
from users.models import User

class loanSerializer(serializers.ModelSerializer):
    
    username = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    first_guarantor = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    second_guarantor = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
        
    class Meta:
        model = Loan
        fields = '__all__'