from unicodedata import category
from django.contrib import admin
import site
from .models import Product,Brand,Category,ProductImages,ProductReview

class ProductImageTabular(admin.TabularInline):
    model = ProductImages

class ProductTabular(admin.TabularInline):
    model = Product
    fields = ['name']

class BrandTabular(admin.TabularInline):
    model = Brand

class ProductImageAdmin(admin.ModelAdmin):
    inlines = [ProductImageTabular]
    list_display = ['name', 'flag', 'quantity', 'price']
    list_filter = ['flag','quantity']
    search_fields = ['name' , 'desc' , 'subtitle']

class BrandAdmin(admin.ModelAdmin):
    inlines = [BrandTabular]

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductTabular]  

# Register your models here.
admin.site.register(Product,ProductImageAdmin)
admin.site.register(Brand,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Category,BrandAdmin)
admin.site.register(ProductReview)
