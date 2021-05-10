from django.db import models
from django.utils import timezone
from product.models import Product
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Retailer(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    country = CountryField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.user.name




class Outlet(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
    )
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, blank=False, null=False, related_name='outlet')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outlet')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    outlet_type = models.CharField(max_length=200)
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

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name





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
