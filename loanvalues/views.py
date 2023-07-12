from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import numpy_financial as npf
import numpy as np
import json
from django.http import JsonResponse
from .serializers import loanValueSerializer , loanValueSerializer2 , LoanValueSerializer
from .models import loanValue
from rest_framework import generics

# Create your views here.

@api_view(['GET'])
def getLoanValues(request , loan_number ):
    loan = loanValue.objects.filter(loan_number=loan_number).all()
    serializer = loanValueSerializer(loan , many=True)
    return Response(serializer.data)
    

class LoanValueCreateView(generics.CreateAPIView):
    def post(self , request , *args , **kwargs):
        data = request.data
        loan_number = data['loan_number']
        loan = loanValue.objects.filter(loan_number=loan_number).all()
        if len(loan) > 0:
            loan.delete()
        loan = LoanValueSerializer(data=data)
        if loan.is_valid():
            loan.save()
            return Response(loan.data)
        return Response(loan.errors)

class getAllLoans(generics.ListAPIView):
    queryset = loanValue.objects.all()
    serializer_class = loanValueSerializer2