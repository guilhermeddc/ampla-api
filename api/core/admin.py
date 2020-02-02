from django.contrib import admin
from .models import Category, Product, ProductComments, Provider

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductComments)
admin.site.register(Provider)
