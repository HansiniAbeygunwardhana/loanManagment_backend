from django.shortcuts import render
from .serializers import loanSerializer
from rest_framework.response import Response
from .models import Loans
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getLoans(request):
    user = request.user
    loans = user.loans_set.all()
    serializer = loanSerializer(loans, many=True)
    return Response(serializer.data)