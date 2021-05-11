from django.db import models
from django.utils import timezone
from product.models import Product
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from mptt.models import MPTTModel, TreeForeignKey

class Retailer(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name



class OutletType(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name



class Outlet(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
    )
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, blank=False, null=False, related_name='outlet')
    outlet_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    outlet_type = models.ForeignKey(OutletType, on_delete=models.CASCADE, blank=False, null=False, related_name='outlet')
    address = models.CharField(max_length=200)
    country = CountryField()
    county = models.CharField(max_length=200)
    constituency = models.CharField(max_length=200)
    ward = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    gps_coordinates = models.CharField(max_length=200)
    outlet_code = models.CharField(max_length=200)
    outlet_person = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    amenities = models.TextField(max_length=200)
    staff_recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outlet')
    status =  models.CharField(max_length=12, choices=STATUS_CHOICES, default='deactivated')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
 

    class Meta:
        ordering = ('outlet_name',)


    def __str__(self):
        return self.outlet_name





class Transaction(models.Model):
    TYPE_CHOICES = (
        ('in', 'Stock In'),
        ('out', 'Stock Out'),
    )
    quantity=models.IntegerField()
    time=models.DateTimeField(auto_now=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    outlet=models.ForeignKey(Outlet, on_delete=models.CASCADE, blank=False, null=False)
    tran_type =  models.CharField(max_length=12, choices=TYPE_CHOICES, default='in')

    class Meta:
        ordering = ('-time',)
