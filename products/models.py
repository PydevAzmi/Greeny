
from email.policy import default
from itertools import count
from msilib.schema import Class
from operator import imod
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator , MinValueValidator
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.db.models.aggregates import Count
# Create your models here.


FLAG_OPTION = (
    ('New','New'),
    ('Feature','Feature'),
    ('Sale','Sale'),
)


class Product(models.Model):
    name = models.CharField(max_length=100 , verbose_name=_("Name"))
    subtitle = models.CharField(_("Subtitle"),max_length=500)
    sku = models.IntegerField(_("SKU"))
    image = models.ImageField(_("Image"), upload_to='products/product_images/')
    desc = models.TextField(_("Description"),max_length=10000)
    price = models.FloatField(_("Price"))
    flag = models.CharField(_("Flag") , max_length=10 , choices=FLAG_OPTION)
    quantity = models.IntegerField(_("Quantity")) 
    brand = models.ForeignKey('Brand', verbose_name=_('Brand'), related_name='product_brand', on_delete=models.SET_NULL , null = True , blank=True )
    category = models.ForeignKey('Category', verbose_name='Category' , related_name='product_category' , on_delete=models.SET_NULL , null = True , blank=True ) 
    tags = TaggableManager()
    # add slug to url 
    slug = models.SlugField(_("Slug"),null=True , blank= True)
    
      
    def __str__(self):
        return self.name

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args, **kwargs)


    

    



class ProductImages(models.Model):
    product = models.ForeignKey( Product, related_name='product_image', on_delete=models.CASCADE, verbose_name=_("Product"))
    image  = models.ImageField(_("Image"), upload_to='products/product_images/')


    def __str__(self):
        return str(self.product)




class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"), upload_to ='products/brands/')
    category = models.ForeignKey('Category', related_name='brand_category', verbose_name=_('Category'),on_delete=models.CASCADE )

    def __str__(self):
        return self.name

    def product_count(self):
        return self.product_brand.aggregate(my_count = Count('brand'))
        



class Category(models.Model):
    name= models.CharField(_("Name") ,max_length=50  )
    image = models.ImageField(_("Image"), upload_to ='products/category/')

    def __str__(self):
        return self.name




class ProductReview(models.Model):
    user = models.ForeignKey(User, related_name='user_review', on_delete=models.CASCADE, verbose_name=_("User") )
    product = models.ForeignKey(Product, related_name='product_review', on_delete=models.CASCADE, verbose_name=_("Product"))
    rate = models.IntegerField(_("Rate"),validators=[MaxValueValidator(5),MinValueValidator(0)] )
    review  = models.CharField(_("Review"), max_length=500 )
    created_at = models.DateTimeField(verbose_name=_("Created_At"),default=timezone.now)


    def __str__(self):
        return str(self.user )+'Review on ' + str(self.product)













