from django.contrib import admin
from .models import Retailer, Outlet, Transaction, OutletType
from django_mptt_admin.admin import DjangoMpttAdmin

admin.site.register(Transaction)



@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ('name',  'mobile', 'email', 'status', 'created')
    list_filter = ('name', 'status')
    list_editable = ['status']
    search_fields = ('name', 'status')
    date_hierarchy = 'created'
    
    ordering = ('status', 'created')



@admin.register(Outlet)
class OutletAdmin(admin.ModelAdmin):
    list_display = ('outlet_name', 'retailer', 'outlet_type', 'outlet_code',  'country', 'status')
    list_filter = ('outlet_name', 'country', 'outlet_type')
    list_editable = ['status']
    search_fields = ('outlet_name', 'outlet_type')
    date_hierarchy = 'created'
    ordering = ('outlet_name', 'created')
    prepopulated_fields = {'slug': ('outlet_name',)}


@admin.register(OutletType)
class OutletTypeAdmin(DjangoMpttAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}