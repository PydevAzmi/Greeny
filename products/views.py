from __future__ import annotations
from itertools import product
from multiprocessing import get_context
from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product ,Brand, Category ,ProductImages 
from django.db.models.aggregates import Count
from django.db.models import Value ,F

# Create your views here.

# Function Based View
def prodcut_list(request):
    # products = Product.objects.all()                                  # All products with out filter
    # products = Product.objects.filter(price__lte = 50 )               # greater than or equal 
    # products = Product.objects.filter(price__gte = 50 )               # less than or equal
    # products = Product.objects.filter(price__gt = 50 )                # greater than
    # products = Product.objects.filter(price__lt = 50 )                # less than
    
    products = Product.objects.filter(price__gt = 50 )
    return render(request, 'products/product_list_test.html', {'products':products})

# Class Based View  
class ProductList(ListView):
    model = Product
    paginate_by = 12
    # ListView ^-^
    # context  -> product_list or object_list
    # templete -> must named -> product_list.html 

class ProductDetail(DetailView):
    model= Product

    # DetailView ^-^
    # context  -> product_detail or object_detail
    # templete -> must named -> product_detail.html 


class BrandList(ListView):
    model = Brand
    

    # override get_context_data with other context  
    def get_context_data(self, **kwargs):
        # we use super() funtion to run the two methods -first in ListView, -second on BrandList ( in this class )
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all
        # select_related() to prevent doing more queirs for each category 
        context["brand_list"] = Brand.objects.select_related('category').all().annotate(product_count=Count('product_brand'))
        return context
    


class BrandDetail(DetailView):
    model = Brand 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context['product_brand'] = Product.objects.filter(brand=brand)
        context['number'] = brand.product_count()
        return context
    


class CategoryList(ListView):
    model = Category