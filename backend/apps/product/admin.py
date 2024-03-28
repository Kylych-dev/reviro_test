from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'description', 'price', 'quantity_in_stock')
    search_fields = ('name',)
    list_filter = ('price', 'quantity_in_stock')

    