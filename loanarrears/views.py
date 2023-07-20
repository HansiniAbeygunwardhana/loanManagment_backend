from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import loanArrearsSerializerBasic , loanArrearsSerializer
from rest_framework import status
from .models import loanarrears
from django_filters import rest_framework as filters
from rest_framework import generics
from django.db.models import Max
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
        queryset = loanarrears.filter_by_loanaddress(location=location)
        return queryset