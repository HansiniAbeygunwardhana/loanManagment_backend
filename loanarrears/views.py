from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import loanArrearsSerializerBasic , loanArrearsSerializer
from rest_framework import status

# Create your views here.

class AddArrears(APIView):
    def post(self, request):
        serializer = loanArrearsSerializerBasic(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Failed to add arrears", status=status.HTTP_400_BAD_REQUEST)