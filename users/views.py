from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomerUsernameSerializer
from managers.serializers import ManagerSerializer
from customers.serializers import CustomerSerializer
from staff.serializers import StaffSerializer
from rest_framework import status
from users.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['user_type'] = user.user_type
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['POST'])
def customer_registration(request):
    serializer = CustomerSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user_type='customer')
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def manager_registration(request):
    serializer = ManagerSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user_type='manager')
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def staff_registration(request):
    serializer = StaffSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user_type='staff')
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def getCustomers(request):
    customer_users = User.objects.filter(user_type='customer')
    serializer = CustomerUsernameSerializer(customer_users, many=True)
    
    return Response(serializer.data, status=200)