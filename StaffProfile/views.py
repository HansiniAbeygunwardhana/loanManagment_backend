from django.shortcuts import render
from .serializers import StaffProfileSerializer , StaffSerializerByName
from .models import StaffProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from  loanarrears.models import loanarrears
from django.utils import timezone

def get_current_date():
    current_date = timezone.now().date()
    return current_date.strftime("%Y-%m-%d")

def get_current_month_and_day():
    current_date = timezone.now().date()
    return current_date.strftime("%m-%d")


class ListStaff(APIView):
    def get(self, request):
        staff = StaffProfile.objects.all()
        serializer = StaffProfileSerializer(staff, many=True)
        return Response(serializer.data)
    

class AddStaff(APIView):
    def post(self, request):
        serializer = StaffProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)
        return Response(serializer.errors , status=400)
    
class GetStaffById(APIView):
    def get(self, request , id):
        staff = StaffProfile.objects.get(user_id=id)
        serializer = StaffSerializerByName(staff)
        return Response(serializer.data)
    
class GetStaffHome(APIView):
    def get(self, request , id):
        
        
        try:
            current_date = get_current_date()
            current_month_and_day_str = get_current_month_and_day()
            staff = StaffProfile.objects.get(user_id=id)
            loan_arrears = loanarrears.objects.filter(staff_id=staff.id).exclude(monthly_arrears=0)
            loan_arrears_details = []
            loan_arrears_current_date = loan_arrears.filter(loan_id__loaned_date__icontains=current_month_and_day_str)
               
            loan_arrears_current_date_details = []
            
            for loan in loan_arrears:
                loan_arrears_item = {
                    "loan_number" : loan.loan_id.loan_number,
                    "customer_name" : loan.loan_id.username.name,
                    "loan_arrears_amount" : loan.monthly_arrears,
                }
                loan_arrears_details.append(loan_arrears_item)
            
            if loan_arrears_current_date:
                print(loan_arrears_current_date)    
                for loan in loan_arrears_current_date:
                    item = {
                        "loan_number" : loan.loan_id.loan_number,
                        "loan_arrears_amount" : loan.monthly_arrears,
                    }
                    loan_arrears_current_date_details.append(item)
            else:
                loan_arrears_current_date_details = []
                
            data = {
                "staff_name" : staff.name.split()[0],
                "loan_arrears" : loan_arrears_details,
                "current_date" : current_date,
                "loan_arrears_today" : loan_arrears_current_date_details,
                "arrears_count" : loan_arrears.count(),
            }
            
        
            return Response(data , status=200)
        
        except:
            return Response({'message' : 'No staff found'} , status=400)