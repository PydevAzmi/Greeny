from django.urls import path
from .views import BrandDetail, BrandList, ProductList, ProductDetail, CategoryList, prodcut_list
from . import api
app_name = 'products'


urlpatterns = [
    path('' , ProductList.as_view() , name='product_list'),
    path('<int:pk>/',ProductDetail.as_view() , name='product_detail' ),
    path('brands/' , BrandList.as_view() , name='brand_list'),
    path('brands/<int:pk>/',BrandDetail.as_view() , name='brand_detail' ),
    path('category/',CategoryList.as_view(),name = 'category_list'),
    path('testing/', prodcut_list  ),


    path('api/products/<int:pk>',api.ProductDetailAPI.as_view()),
    path('api/products/',api.ProductListAPI.as_view()),
    path('api/brand/', api.BrandListAPI.as_view()),
    path('api/brand/<int:pk>', api.BrandDetailAPI.as_view()),
    path('api/category/',api.CategoryListAPI.as_view()),
    path('api/category/<int:pk>',api.CategoryDetailAPI.as_view()),


]
