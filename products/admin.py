from django.contrib import admin
import site
from .models import Product,Brand,Category,ProductImages,ProductReview

class ProductImageTabular(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageTabular]
    list_display = ['name', 'flag', 'category',  'quantity', 'price']
    list_filter = ['flag','category']
    search_fields = ['name' , 'desc' , 'subtitle']

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(ProductImages)
admin.site.register(Category)
admin.site.register(ProductReview)
