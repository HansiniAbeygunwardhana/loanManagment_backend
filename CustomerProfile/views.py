from django.shortcuts import render
from .serializers import CustomerProfileSerializer , CustomerNameIDSerializer , CustomerProfileOnlySerializer
from .models import CustomerProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser , JSONParser
from django.shortcuts import get_object_or_404
# Create your views here.

class ListCustomer(APIView):
    def get(self, request):
        customer = CustomerProfile.objects.all()
        serializer = CustomerProfileSerializer(customer, many=True)
        return Response(serializer.data)
    

class AddCustomer(APIView):
    
    parser_classes = (MultiPartParser, FormParser , JSONParser)
    
    def post(self, request):
        serializer = CustomerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)
        print(serializer.errors)
        return Response(serializer.errors , status=400)
    
    
class ListCustomerNames(APIView):
    def get(self, request):
        customer = CustomerProfile.objects.all()
        serializer = CustomerNameIDSerializer(customer, many=True)
        return Response(serializer.data)
    
class GetOneCustomer(APIView):
    def get(self, request, id):
        customer = get_object_or_404(CustomerProfile, id=id)
        serializer = CustomerProfileOnlySerializer(customer)
        return Response(serializer.data)