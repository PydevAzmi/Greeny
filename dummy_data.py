from itertools import product
import os
from unicodedata import category
from webbrowser import get
import django
# Set environment variable > Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

# Add our code :
import random
from products.models import Product,Category,Brand ,ProductImages
from faker import Faker


def seed_category(n):
    fake = Faker()
    images = ['1.webp','2.jpg','3.webp','4.webp','5.webp','6.jpg']
    
    for _ in range(n):
        name = fake.name()
        image = f"products/category/{images[random.randint(0,5)]}"
        Category.objects.create(
            name = name,
            image = image
        )
    print(f"successfuilly added {n} category")



def seed_brand(n):
    fake = Faker()
    images = ['1.png', '3.png','5.jpg','7.jpg','8.jpg','9.jpg',
              '10.jpg','11.jpg','12.jpg','2.jfif','4.jfif','6.gif']
    for _ in range(n):
        name = fake.name()
        image = f"products/brands/{images[random.randint(0,11)]}"
        Brand.objects.create(
            name = name, 
            image = image,
            # cahnge range numbers with corrrect id in next time
            category = Category.objects.get(id = random.randint(13,22))
        )
    print(f"sucessfully added {n} Brands")

def seed_product(n):
    fake = Faker()
    images = [
        '1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg',
        '10.jpg','11.jpg','12.jpg','12.jpg','14.jpg','15.jpg','16.jpg',
        '17.jpg','18.jpg','19.jpg','20.jpg','21.jpg','22.jpg','23.jpg',
    ]
    flag_options = ['New','Feature','Sale']
    for _ in range(n):
        name = fake.name()
        image = f"products/product_images/{images[random.randint(0,22)]}"
        subtitle = fake.text(max_nb_chars=500)
        sku = random.randint(1000,100000) 
        description = fake.text(max_nb_chars=1000 ) 
        price =round( random.uniform(20.99,99.99),2)
        flag = flag_options[random.randint(0,2)]
        quantity = random.randint(1,100)
        
        Product.objects.create(
            name = name, 
            subtitle = subtitle,
            sku = sku ,  
            image = image,
            desc = description,
            price =price,
            flag = flag,
            quantity = quantity,
            # cahnge range numbers with corrrect id in next time
            brand = Brand.objects.get(id = random.randint(23,62)),       # id -> 23 : 62 + ( n if you add brands)
            category = Category.objects.get(id = random.randint(13,22))  # id -> 13 : 22 + ( n if you add categories)

        )
    print(f"successfuilly added {n} products")

def seed_ProductImages():
    images = [
        '1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg',
        '10.jpg','11.jpg','12.jpg','12.jpg','14.jpg','15.jpg','16.jpg',
        '17.jpg','18.jpg','19.jpg','20.jpg','21.jpg','22.jpg','23.jpg',
    ]
    
    for i in range(220,720):
        
        image = f"products/product_images/{images[random.randint(0,22)]}"

        ProductImages.objects.create(
            product = Product.objects.get( id= i),
            image = image
        )

    print(f"successfuilly added {i-220} products Images")


## to add data :
#seed_ProductImages()
#seed_category(10)
#seed_brand(20)
#seed_product(100)




