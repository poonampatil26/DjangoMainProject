from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list = ['id','provider','name_of_product','price','quantity','amount','stock']

admin.site.register(Product,ProductAdmin)
