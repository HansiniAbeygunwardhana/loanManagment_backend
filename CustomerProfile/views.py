from django.shortcuts import render
from .serializers import CustomerProfileSerializer , CustomerNameIDSerializer , CustomerProfileOnlySerializerWithId,BasicCustomerData, CustomerProfileOnlySerializer , CustomerImageOnlySerializer , HomeScreenCustomerSerializer
from .models import CustomerProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser , JSONParser
from django.shortcuts import get_object_or_404
from loans.models import Loan
from loanvalues.models import loanValue
from loanarrears.models import loanarrears
# Create your views here.

class ListCustomer(APIView):
    def get(self, request):
        customer = CustomerProfile.objects.all()
        serializer = CustomerProfileSerializer(customer, many=True)
        return Response(serializer.data)
    

class AddCustomer(APIView):
    
    parser_classes = (MultiPartParser, FormParser , JSONParser)
    
    def post(self, request):
        serializer = CustomerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)
        print(serializer.errors)
        return Response(serializer.errors , status=400)
    
    
class ListCustomerNames(APIView):
    def get(self, request):
        customer = CustomerProfile.objects.all()
        serializer = CustomerNameIDSerializer(customer, many=True)
        return Response(serializer.data)
    
class GetOneCustomer(APIView):
    def get(self, request, id):
        customer = get_object_or_404(CustomerProfile, id=id)
        serializer = CustomerProfileOnlySerializerWithId(customer)
        return Response(serializer.data)
    
class UpdateCustomerImage(APIView):
    def put(self, request, id):
        customer = get_object_or_404(CustomerProfile, id=id)
        serializer = CustomerImageOnlySerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request, id):
        customer = get_object_or_404(CustomerProfile, id=id)
        serializer = CustomerImageOnlySerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    

class GetDataCustomerHome(APIView):
    def get(self, request, id):
        try : 
            customer = get_object_or_404(CustomerProfile, user_id=id)
            loan = Loan.objects.get(username=customer)
            loanpayments = loanValue.objects.filter(loan_number=loan.loan_id).order_by('-id').first()
            loanarrearsdata = loanarrears.objects.filter(loan_id=loan.loan_id).order_by('-id').first()
            
            if loanpayments:
                last_payment = loanpayments.payment_amount
                last_payment_date = loanpayments.payment_date
            else:
                last_payment = 0.0
                last_payment_date = None
            
            if loanarrearsdata:
                arrears = loanarrearsdata.monthly_arrears
                arr_cal_date = loanarrearsdata.arr_cal_date
            else:
                arrears = 0.0
                arr_cal_date = None
            
            data = {
                "loan_id" : loan.loan_id,
                "loan_number" : loan.loan_number,
                "customer_id" : customer.id,
                "customer_name" : customer.name,
                "customer_address" : customer.address,
                "profileimage" : customer.profileimage.url,
                "loaned_amount" : loan.loaned_amount,
                "last_payment" : last_payment,
                "last_payment_date" : last_payment_date,
                "arrears" : arrears,
                "arrears_date" : arr_cal_date,
                "monthly_payment" : loanarrearsdata.monthly_payment,
                
            }
            
            return Response(data=data , status=200)
        
        except CustomerProfile.DoesNotExist:
            return Response(status=404 , data={'message' : 'Customer does not exist'})
        except Loan.DoesNotExist:
            return Response(status=404 , data={'message' : 'Loan does not exist'})
        except loanValue.DoesNotExist:
            return Response(status=404 , data={'message' : 'No loan payments found'})
        except loanarrears.DoesNotExist:
            return Response(status=404 , data={'message' : 'No loan arrears found'})
        

class ListBasicCustomerData(APIView):
    def get(self, request):
        
        try:
            customers = CustomerProfile.objects.all()
            
            customer_data = []
            
            for customer in customers:
                loan = Loan.objects.filter(username_id=1).first()
                
                print(loan.branch_location)
                if loan:
                    loan_number = loan.loan_number
                else:
                    loan_number = None
                
                item = {
                    "name" : customer.name,
                    "telephone1" : customer.telephone1,
                    "nicnumber" : customer.nicnumber,
                    "loan_number" : loan_number,
                    "loan_id" : str(loan.loan_id),
                    "customer_id" : str(customer.id),
                }
                
                customer_data.append(item)
                
            return Response(customer_data, status=200)
        
        except:
            return Response(status=404 , data={'message' : 'Customer does not exist'})
    
            
        
            