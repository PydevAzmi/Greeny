from multiprocessing import get_context
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product ,Brand, Category
from django.db.models.aggregates import Count
# Create your views here.


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model= Product


class BrandList(ListView):
    model = Brand
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all
        context["brand_list"] = Brand.objects.all().annotate(product_count=Count('product_brand'))
        return context
    


class BrandDetail(DetailView):
    model = Brand


class CategoryList(ListView):
    model = Category