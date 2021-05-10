from django.contrib import admin
from .models import Agent, Retailer, Outlet, Transaction

admin.site.register(Retailer)
admin.site.register(Outlet)
admin.site.register(Transaction)
admin.site.register(Agent)