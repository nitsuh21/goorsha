from typing import Any
from django.shortcuts import render
from requests import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserSerializer    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserSignupView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Additional logic for user signup if needed
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            # Additional logic after successful user signup
            pass
        return response

    def get(self, request, *args, **kwargs):
        return Response("Method 'GET' not allowed.")

    def put(self, request, *args, **kwargs):
        return Response("Method 'PUT' not allowed.")

    def patch(self, request, *args, **kwargs):
        return Response("Method 'PATCH' not allowed.")

    def delete(self, request, *args, **kwargs):
        return Response("Method 'DELETE' not allowed.")
