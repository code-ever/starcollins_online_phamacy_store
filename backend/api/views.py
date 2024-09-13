from django.shortcuts import render
from .models import Profile, Category, UploadProduct
from rest_framework import generics
from .Serializers import CategorySerializer, UploadSerializer
# Create your views here.

class ProductView(generics.ListCreateAPIView):
    queryset = UploadProduct.objects.all()
    serializer_class = UploadSerializer
    
    
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
