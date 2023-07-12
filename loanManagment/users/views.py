from django.shortcuts import render
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserViewSet(APIView):
    
    def get(self ,  request , format=None):
        queryset = CustomUser.objects.all()
        serializer_class = UserSerializer(queryset , many=True)
        return Response(serializer_class.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)   
        return Response(serializer.data)
