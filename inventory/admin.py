from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("sku", "name", "price", "stock", "created_at")
    search_fields = ("sku", "name")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity", "created_at")