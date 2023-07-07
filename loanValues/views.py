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
    queryset = loanValue.objects.all()
    serializer_class = LoanValueSerializer

class getAllLoans(generics.ListAPIView):
    queryset = loanValue.objects.all()
    serializer_class = loanValueSerializer2
