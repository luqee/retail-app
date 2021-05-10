from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    return 'products/%Y/%m/%d/'.format(instance.id, filename)

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True)
    sku = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    image = models.ImageField( upload_to=user_directory_path, default='products/default.jpg')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (0, 'anon'),
        (1, 'retailer'),
        (2, 'agent'),
        (3, 'admin'),
    )

    role = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=0)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length=200)

    # class Meta:
    #     ordering = ('name',)


    def __str__(self):
        return self.user.name

class Retailer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    # class Meta:
    #     ordering = ('name',)


    def __str__(self):
        return self.user.name

class Outlet(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
    )
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, blank=False, null=False, related_name='outlet')
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
