from django.shortcuts import render
from requests import Response
from rest_framework.views import APIView
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserSerializer    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserSignupView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                serializer.data['username'],
                serializer.data['email'],
                serializer.data['password']
            )
            user.save()
            return Response(serializer.data)
        return Response(serializer.errors)