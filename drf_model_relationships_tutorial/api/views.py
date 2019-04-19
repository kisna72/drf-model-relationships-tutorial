from django.shortcuts import render
from rest_framework import generics
from api.serializers import ProductSerializer
from api.models import Product


# Create your views here.
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
