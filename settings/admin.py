from django.contrib import admin
import site
# Register your models here.

from .models import Company

admin.site.register(Company)