from django.shortcuts import render
from .serializers import loanSerializer , simpleLoanSerializer , loanSerializerCustomerId, loanNumbererializer ,  loanIDandNumberSerializer, loanSerializerExtended
from rest_framework.response import Response
from .models import Loan
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from CustomerProfile.models import CustomerProfile
from loanvalues.models import loanValue
from loanarrears.models import loanarrears
# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getLoans(request):
    #user = request.user
   # loan = user.loans_set.all()
    loan = Loan.objects.all()
    serializer = simpleLoanSerializer(loan, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addLoans(request):
    serializer = loanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Added Successfully")

@api_view(['GET'])
def getMoreLoanDetails(request, loan_id):
    try:
        loan = Loan.objects.get(loan_id=loan_id)
        serializer = loanSerializer(loan)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response("Loan Not Found", status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAllLoanNumbers(request):
    loan = Loan.objects.all()
    serializer = loanNumbererializer(loan, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getALLLoansbyUserID(request , user_id):
    loan = Loan.objects.get(username_id=user_id)
    serializer = loanNumbererializer(loan)
    return Response(serializer.data)

class getAllLoans(generics.ListAPIView):
    queryset = Loan.objects.all()
    serializer_class = loanIDandNumberSerializer
 
@api_view(['GET'])   
def getLoansByLoanNumber(request, loan_number):
    try:
        loan = Loan.objects.get(loan_number=loan_number)
        serializer = loanSerializerExtended(loan)  # Ensure that the serializer class name is correct (LoanSerializer)
        return Response(serializer.data)
    except Loan.DoesNotExist:
        return Response({'error': 'Loan not found'}, status=404)
    

class LoanUsernameAPIView(APIView):
    def get(self, request,  loan_number):
        try:
            loan = Loan.objects.get(loan_number=loan_number)
            serializer = loanSerializerCustomerId(loan)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Loan.DoesNotExist:
            return Response({"error": "Loan number not found"}, status=status.HTTP_404_NOT_FOUND)
        
class ListWebDataView(APIView):
    def get(self, request , loan_id):
        try: 
            loans = Loan.objects.get(loan_id=loan_id)
            customers = CustomerProfile.objects.get(id=loans.username_id)
            payments = loanValue.objects.filter(loan_number=loans.loan_id).latest('id')
            loanarrearsdata = loanarrears.objects.filter(loan_id=loans.loan_id).latest('id')
        
        
            data ={
                'loan_number': loans.loan_number,
                'loan_id' : loans.loan_id,
                'customer_name' : customers.name,
                'customer_image' : customers.profileimage.url,
                'last_payment_amount' : payments.payment_amount,
                'last_payment_date' : payments.payment_date,
                'monthly_payment' : loanarrearsdata.monthly_payment,
                'customer_id' : customers.id,
                
                
            }
            
            return Response(data, status=status.HTTP_200_OK)
        
        except:
            return Response({"error": "Loan number not found"}, status=status.HTTP_404_NOT_FOUND)
    
