from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User
from .serializers import CustomerSerializer
from .models import Customer
# Create your views here.


@api_view(['GET'])
def getCustomers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addCustomers(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Added Successfully")

