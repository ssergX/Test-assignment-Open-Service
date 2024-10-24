from django.contrib import admin
from .models import Product, ProductType, Price


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'barcode', 'last_updated', 'product_type')
    search_fields = ('name', 'barcode')


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('currency', 'amount')



