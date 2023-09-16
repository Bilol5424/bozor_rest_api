from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer

class UserListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create your views here.
