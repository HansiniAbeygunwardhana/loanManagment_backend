from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializers
from .models import User
import jwt,datetime
from django.views.decorators.csrf import get_token 
from django.middleware.csrf import CsrfViewMiddleware

# Create your views here.

class get_CSRF_Token(APIView):
    
        def get(self, request):
        # Get the CSRF token
            csrf_token = get_token(request)
            print(csrf_token)
        # Return the CSRF token in the response
            return Response({'csrfToken': csrf_token})


class RegisterView(APIView):
    
    def post(self , request):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    
    def dispatch(self, request, *args, **kwargs):
        csrf_middleware = CsrfViewMiddleware()
        # Process the request through the CSRF middleware to set the CSRF cookie
        request = csrf_middleware.process_view(request, None, (), {})
        return super().dispatch(request, *args, **kwargs)   
    
    
    def post(self,request):
        
        if not request.COOKIES.get('csrftoken'):
            raise AuthenticationFailed('CSRF cookie not set.')
        
        username = request.data['username']
        password = request.data['password']
        
        user = User.objects.filter(username = username).first()
        
        if user is None:
            raise AuthenticationFailed("User not found")
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        
        payload = {
            'id':  user.id,
            'exp':  datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':  datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload , 'secret' , algorithm='HS256' )
        
        response = Response()
        
        response.set_cookie(key='jwt' , value=token , httponly=True)
        response.data = {
            'jwt': token
        }
        
        return response

class UserView(APIView):
    def get(self ,request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try :
            payload = jwt.decode(token, 'secret' , algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenitcated')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializers(user)
        return Response(serializer.data)
        