from re import search
from unicodedata import category
from winreg import QueryInfoKey
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializer import ProductSerializer ,BrandSerializer, CategorySerializer
from .models import Brand, Product, Category


#### using Functions ####
# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()[:10]
#     data = ProductSerializer(products,many=True).data
#     return Response({'Success':True, 'Product List': data})


# @api_view(['GET'])
# def product_detail(request,id):
#     product = Product.objects.get(id=id)
#     data = ProductSerializer(product).data
#     return Response({'Success':True , 'Product': data})


#### using Generic Views ####
# rest_framework import Generics
from rest_framework import generics
import django_filters.rest_framework
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from products import serializer 



class ProductListAPI(generics.ListAPIView):
    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    #--- Rest-Framework ---#
    #-28 Filter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'brand']

    #-29 Search Filter
    #filter_backends = [SearchFilter]
    search_fields = ['name']

    # Authentication
    permission_classes = [IsAuthenticated]


class ProductDetailAPI(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class BrandListAPI(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name']

class BrandDetailAPI(generics.RetrieveAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, SearchFilter]
    search_fields = ['name']

class CategoryDetailAPI(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
