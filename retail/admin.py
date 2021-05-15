from django.contrib import admin
from .models import User as AppUser, Recruiter, Retailer, Outlet, OutletType, ProductCategory, Product, Brand

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# class RecruiterUserInline(admin.StackedInline):
#     model = AppUser

# class RetailerUserInline(admin.StackedInline):
#     model = AppUser

# @admin.register(AppUser)
# class RecruiterAdmin(admin.ModelAdmin):
#     inlines=[RecruiterUserInline]

@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    pass

@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',  'slug', 'bar_code', 'unit_type', 'image', 'description', 'available', 'created', 'updated')
    list_filter = ('created', 'updated', 'name')
    list_editable = ['available']
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created'
    ordering = ('name', 'created')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Outlet)
class OutletAdmin(admin.ModelAdmin):
    # list_display = ('outlet_name', 'retailer', 'outlet_type', 'outlet_code',  'country', 'status')
    # list_filter = ('outlet_name', 'country', 'outlet_type')
    # list_editable = ['status']
    # search_fields = ('outlet_name', 'outlet_type')
    # date_hierarchy = 'created'
    # ordering = ('outlet_name', 'created')
    # prepopulated_fields = {'slug': ('outlet_name',)}
    pass

@admin.register(OutletType)
class OutletTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}