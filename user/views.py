"""
User app views for user related functionalities 
Views for User/Admin Registration and Custom Auth Tokens creation for authentication
"""

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserRegistrationSerializers, AdminRegistrationSerializer
from rest_framework.generics import CreateAPIView
from .models import User


class CustomAuthToken(ObtainAuthToken):
    """
    creates or fetch auth tokens upon correct credentials
    username->email
    password->related password
    returns-> {
                'token':token.key,
                'user email':user.email,
                'name':user.name
            }
    """
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={
                'request':request
                }
            )
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token':token.key,
                'user email':user.email,
                'name':user.name
            })
        
        return Response(serializer.errors)


class UserRegistrationView(CreateAPIView):
    """
    User registration, creates users who can request for loan
    Method -> POST
    input arguments-> email,name,password
    returns -> created user
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers


class AdminRegistrationView(CreateAPIView):
    """
    Admin registration, creates admins who approve/delcine loan requests
    Method -> POST
    input arguments-> email,name,password
    returns -> created user
    """
    queryset = User.objects.all()
    serializer_class = AdminRegistrationSerializer