from django.shortcuts import render
from .serializers import StaffProfileSerializer , StaffSerializerByName
from .models import StaffProfile
from rest_framework.views import APIView
from rest_framework.response import Response

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