from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from places.fields import PlacesField

class User(AbstractUser):
    # recruiter = models.OneToOneField('Recruiter', on_delete=models.CASCADE, null=True, related_name='user')
    # retailer = models.OneToOneField('Retailer', on_delete=models.CASCADE, null=True, related_name='user')
    is_recruiter = models.BooleanField(default=False)
    is_retailer = models.BooleanField(default=False)

class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    mobile = models.CharField(max_length=200)
    id_number = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)


    # class Meta:
    #     ordering = ('name',)


    def __str__(self):
        return self.user.username

class Retailer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    mobile = models.CharField(max_length=200)
    registered_by = models.ForeignKey(Recruiter, on_delete=models.CASCADE, blank=False, null=False, related_name='retailers')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)


    # class Meta:
    #     ordering = ('name',)


    def __str__(self):
        return self.user.username

class OutletType(models.Model):
    name = models.CharField(max_length=200)
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
    owner = models.OneToOneField(Retailer, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    outlet_type = models.ForeignKey(OutletType, on_delete=models.CASCADE, blank=False, null=False, related_name='outlets')
    address = models.CharField(max_length=200)
    country = CountryField()
    county = models.CharField(max_length=200)
    constituency = models.CharField(max_length=200)
    ward = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    location = PlacesField()
    # latitude = models.DecimalField(max_digits=9, decimal_places=6)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6)
    outlet_code = models.CharField(max_length=200)
    outlet_person = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    amenities = models.TextField(max_length=200)
    registered_by = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name='outlets')
    status =  models.CharField(max_length=12, choices=STATUS_CHOICES, default='deactivated')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
 

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)


    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
  

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    return 'products/%Y/%m/%d/'.format(instance.id, filename)


class Product(models.Model):
    UNIT_TYPE_KG = 'Kilogram'
    UNIT_TYPE_GRAM = 'Gram'
    UNIT_TYPE_LITRE = 'Litre'
    UNIT_TYPE_QUANTITY = 'Quantity'

    UNIT_TYPES = (
        (UNIT_TYPE_KG, 'Kilogram'),
        (UNIT_TYPE_GRAM, 'Gram'),
        (UNIT_TYPE_LITRE, 'Litre'),
        (UNIT_TYPE_QUANTITY, 'Quantity'),
    )
   
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False, null=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=False, null=False)
    bar_code = models.CharField(max_length=13, unique=True, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True)
    unit_type = models.CharField(choices=UNIT_TYPES, default=UNIT_TYPE_QUANTITY, blank=True, null=True, max_length=200)
    image = models.ImageField( upload_to=user_directory_path, default='products/default.jpg')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

