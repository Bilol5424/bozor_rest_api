from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Category
from .serializers import CategorySerializer
# from ..python_bozor.custom_authenticators import CustomJWTAuthentication


class CategoryViewSet(viewsets.ModelViewSet):
    # authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Create your views here.
