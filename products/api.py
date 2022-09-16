from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializer import ProductSerializer ,BrandSerializer, CategorySerializer
from .models import Product


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



class ProductList(generics.ListAPIView):
    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetail(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()