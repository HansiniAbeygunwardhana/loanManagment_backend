from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import loanValueSerializer , loanValueSerializer2 , LoanValueSerializer
from .models import loanValue
from rest_framework import generics
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

@api_view(['GET'])
def getLoanValues(request , loan_number ):
    loan = loanValue.objects.filter(loan_number=loan_number).all()
    serializer = loanValueSerializer(loan , many=True)
    return Response(serializer.data)
    

class LoanValueCreateView(generics.CreateAPIView):
    def post(self , request ):
        serializer = LoanValueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)

class getAllLoans(generics.ListAPIView):
    queryset = loanValue.objects.all()
    serializer_class = loanValueSerializer2
    