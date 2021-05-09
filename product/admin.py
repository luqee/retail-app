from django.contrib import admin
from .models import  Product, ProductCategory



admin.site.register(ProductCategory)




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',  'slug', 'image', 'description', 'created', 'updated')
    list_filter = ('created', 'updated', 'name')
    # list_editable = ['featured']
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ('name', 'created')
