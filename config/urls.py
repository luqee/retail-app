from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('retail.urls')),
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'Retail Measurement'