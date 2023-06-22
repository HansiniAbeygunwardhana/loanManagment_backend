from django.shortcuts import render
from .serializers import loanSerializer
from rest_framework.response import Response
from .models import Loan
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getLoans(request):
    #user = request.user
   # loan = user.loans_set.all()
    loan = Loan.objects.all()
    serializer = loanSerializer(loan, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addLoans(request):
    serializer = loanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Added Successfully")