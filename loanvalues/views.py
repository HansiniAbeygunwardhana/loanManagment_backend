from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import loanValueSerializer , loanValueSerializer2 , LoanValueSerializer
from .models import loanValue
from rest_framework import generics
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

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
            loan_value = serializer.save()
            custom_user_email = loan_value.loan_number.username.user.email
            subject = 'Loan Payment'
            from_email = settings.EMAIL_HOST_USER
            html_message = render_to_string('loan_email_template.html', context={'loan_value': loan_value})
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, from_email, [custom_user_email], html_message=html_message)
            return Response(serializer.data , status=201)

class getAllLoans(generics.ListAPIView):
    queryset = loanValue.objects.all()
    serializer_class = loanValueSerializer2
    