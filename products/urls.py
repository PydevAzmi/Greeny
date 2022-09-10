from django.urls import path
from .views import BrandDetail, BrandList, ProductList , ProductDetail ,CategoryList , prodcut_list

app_name = 'products'


urlpatterns = [
    path('' , ProductList.as_view() , name='product_list'),
    path('<int:pk>/',ProductDetail.as_view() , name='product_detail' ),
    path('brands/' , BrandList.as_view() , name='brand_list'),
    path('brands/<int:pk>/',BrandDetail.as_view() , name='brand_detail' ),
    path('category/',CategoryList.as_view(),name = 'category_list'),
    path('testing/', prodcut_list  )

]
