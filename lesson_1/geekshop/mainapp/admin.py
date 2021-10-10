from django.contrib import admin

from .models import ProductCategory, Product, Menu, Telefon

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Menu)
admin.site.register(Telefon)
