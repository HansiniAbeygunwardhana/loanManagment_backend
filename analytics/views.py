from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from .models import analytics
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from loans.models import Loan
from loanvalues.models import loanValue
from loanarrears.models import loanarrears
from CustomerProfile.models import CustomerProfile
from users.models import CustomUser
from analytics.models import analytics

# Create your views here.


class UpdateAnalytics(APIView):
    def post(self, request):
        data = json.loads(request.body)

        # Assuming you're sending an empty JSON object like this: {}
        if not data:
            last_month_date = datetime.now() - relativedelta(months=1)
            last_month_year = last_month_date.strftime("%Y-%m")
            
            existing_record = analytics.objects.filter(calculated_date=last_month_year).first()
            if existing_record:
                # If the record exists, update its values instead of creating a new one
                analytics_instance = existing_record
            else:
                # If the record doesn't exist, create a new one
                analytics_instance = analytics()
                analytics_instance.calculated_date = last_month_year

            # Calculate and set the values
            total_value = 0
            loan_objects = Loan.objects.filter(loaned_date__contains=last_month_year)
            analytics_instance.loan_count = loan_objects.count()

            payments = loanValue.objects.filter(payment_date__contains=last_month_year)
            for payment in payments:
                total_value += payment.payment_amount
            analytics_instance.total_payments = total_value

            loanarrears_objects = loanarrears.objects.filter(arr_cal_date__contains=last_month_year).exclude(monthly_arrears=0)
            analytics_instance.total_loanArrears_accounts = loanarrears_objects.count()

            print(last_month_year)
            print(loanarrears_objects.count())
            user = CustomUser.objects.filter(date_joined__contains=last_month_year)
            monthly_customer = CustomerProfile.objects.filter(user_id__in=user)
            analytics_instance.lastmonth_customer_count = monthly_customer.count()
            analytics_instance.total_loanArrears_accounts = loanarrears_objects.count()
            analytics_instance.date_requested = last_month_year
            analytics_instance.save()

            return JsonResponse({'message': 'Data calculated and saved successfully.'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid data sent. Please send an empty JSON object.'}, status=400)
    
    def get (self , request):
        analytics_records = analytics.objects.all().first()
        serializer = AanalyticsSerializer(analytics_records)
        return Response(serializer.data)
    
class AnalyticsTotalCustomersView(APIView):
    def get (self , request):
        analytics_records = analytics.objects.all().order_by('calculated_date')
        serializer = AnalyticsTotalCustomers(analytics_records , many=True)
        return Response(serializer.data)
    
class AnalyticsTotalLoansView(APIView):
    def get (self , request):
        analytics_records = analytics.objects.all().order_by('calculated_date')
        serializer = AnalyticsTotalLoans(analytics_records , many=True)
        return Response(serializer.data)
    
class AnalyticsTotalPaymentsView(APIView):
    def get (self , request):
        analytics_records = analytics.objects.all().order_by('calculated_date')
        serializer = AnalyticsTotalPayments(analytics_records , many=True)
        return Response(serializer.data)
    
class AnalyticsTotalArrearsView(APIView):
    def get (self , request):
        analytics_records = analytics.objects.all().order_by('calculated_date')
        serializer = AnalyticsTotalArrears(analytics_records , many=True)
        return Response(serializer.data)
    


