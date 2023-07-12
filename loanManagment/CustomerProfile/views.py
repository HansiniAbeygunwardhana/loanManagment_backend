from django.shortcuts import render
from .serializers import CustomerProfileSerializer , CustomerNameIDSerializer
from .models import CustomerProfile
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ListCustomer(APIView):
    def get(self, request):
        customer = CustomerProfile.objects.all()
        serializer = CustomerProfileSerializer(customer, many=True)
        return Response(serializer.data)
    

class AddCustomer(APIView):
    def post(self, request):
        serializer = CustomerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)
        return Response(serializer.errors , status=400)
    
    
class ListCustomerNames(APIView):
    def get(self, request):
        customer = CustomerProfile.objects.all()
        serializer = CustomerNameIDSerializer(customer, many=True)
        return Response(serializer.data)