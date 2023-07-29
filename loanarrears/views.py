from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import loanArrearsSerializerBasic , loanArrearsSerializer, ArrearsCardSerializer
from rest_framework import status
from .models import loanarrears
from django_filters import rest_framework as filters
from rest_framework import generics
from django.db.models import Max
from .utils import loanarrearsuils 
from django.db.models import OuterRef, Subquery
from django.db import models
# Create your views here.

class AddArrears(APIView):
    def post(self, request):
        serializer = loanArrearsSerializerBasic(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Failed to add arrears", status=status.HTTP_400_BAD_REQUEST)
    
class GetArrears(APIView):
    def get(self, request , loan_id):
        arrears = loanarrears.objects.filter(loan_id=loan_id).order_by('-id').first()
        serializer = loanArrearsSerializer(arrears)
        return Response(serializer.data)
    
    
class LoanArrearsFilter(filters.FilterSet):
    loan_id = filters.NumberFilter(field_name='loan_id', distinct=True)
    
    class Meta:
        model = loanarrears
        fields = ['loan_id']

class LoanArrearsList(generics.ListAPIView):
    
    model = loanarrears
    template_name = 'loanarrears.html'
    context_object_name = 'loanarrears'
    serializer_class = loanArrearsSerializer

    def get_queryset(self):
        # Filter the most recent records for each loan_id
        latest_records = loanarrears.objects.values('loan_id').annotate(max_id=Max('id')).values('max_id')
        queryset = loanarrears.objects.filter(id__in=latest_records)
        return queryset
    
class AddAllLoanArrears(APIView):
    def post(self, request):
        arrears_data = request.data
        serializer = loanArrearsSerializerBasic(data=arrears_data , many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Failed to add arrears", status=status.HTTP_400_BAD_REQUEST)
    
class ListLoanArrearsByLocation(generics.ListAPIView):
    
    serializer_class = loanArrearsSerializer
    
    def get_queryset(self):
        location = self.request.query_params.get('location')
        if not location:
            return loanarrears.objects.all()
        queryset = loanarrearsuils.filter_by_loanaddress(location)
        return queryset
    
class FilterLoanArrears(generics.ListAPIView):
    serializer_class = loanArrearsSerializer

    def get_queryset(self):
        location = self.request.query_params.get('location')
        pricemax = self.request.query_params.get('pricemax')
        pricemin = self.request.query_params.get('pricemin')
        latest_records = loanarrears.objects.values('loan_id').annotate(max_id=Max('id')).values('max_id')

        if not (location or pricemax or pricemin):
            latest_records = loanarrearsuils.filter_by_loan_id()
            return latest_records

        queryset = loanarrearsuils.filter_by_location_and_price(location, pricemax, pricemin).exclude(monthly_arrears = 0.0)

        return queryset
    
class FilterLoanArrearsbyStaff(generics.ListAPIView):
    
    serializer_class = ArrearsCardSerializer
    
    def get_queryset(self):
        staffName = self.request.query_params.get('staff')
        
        queryset = loanarrearsuils.filter_by_assigned_staff(staffName=staffName)
        
        return queryset
    
    
    
class LoanArrearsListView(generics.ListAPIView):
    
    serializer_class = loanArrearsSerializer

    def get_queryset(self):
        queryset = loanarrearsuils.filter_by_loan_id()
        return queryset