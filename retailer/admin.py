from django.contrib import admin
from .models import Retailer, Outlet, Transaction

admin.site.register(Outlet)
admin.site.register(Transaction)



@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ('name',  'mobile', 'country')
    list_filter = ('name', 'country')
    list_editable = ['country']
    search_fields = ('name', 'country')
    date_hierarchy = 'created'
    ordering = ('name', 'created')

