from django.contrib import admin
from .models import Retailer, Outlet, Transaction


admin.site.register(Retailer)

admin.site.register(Outlet)

admin.site.register(Transaction)
