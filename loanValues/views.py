from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def calLoanValues(request):
    # Get the values of the two numbers from the request data
    loanAmount = float(request.data.get('loanAmount', 0))
    interestRate = float(request.data.get('interestRate', 0))
    loanMonths = float(request.data.get('loanMonths', 0))
    loanYears = float(request.data.get('loanYears', 0))

    # Perform the addition
    result = loanAmount * (1 + (interestRate/100) * loanYears)

    # Create a response with the result
    response_data = {
        'result': result
    }

    # Return the response
    return Response(response_data)
