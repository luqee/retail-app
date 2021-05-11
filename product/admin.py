from django.contrib import admin
from .models import Product, ProductCategory
from django_mptt_admin.admin import DjangoMpttAdmin


# Register your models here.
@admin.register(ProductCategory)
class ProductCategoryAdmin(DjangoMpttAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',  'slug', 'sku', 'unit_type', 'image', 'description', 'available', 'created', 'updated')
    list_filter = ('created', 'updated', 'name')
    list_editable = ['available']
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created'
    ordering = ('name', 'created')