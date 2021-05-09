from django.db import models
from django.utils import timezone

def user_directory_path(instance, filename):
    return 'products/%Y/%m/%d/'.format(instance.id, filename)


class Retailer(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    country = models.CharField(max_length=200)


    

class Outlet(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    constituency = models.CharField(max_length=200)
    ward = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    gps_coordinates = models.CharField(max_length=200)
    outlet_code = models.CharField(max_length=200)
    outlet_person = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    amenities = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status =  models.CharField(max_length=12, choices=STATUS_CHOICES, default='deactivated')



class ProductCategory(models.Model):
    ...



class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    image = models.ImageField( upload_to=user_directory_path, default='products/default.jpg')



class Transaction(models.Model):
	quantity=models.IntegerField()
	time=models.DateTimeField(auto_now=True)
	product=models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
