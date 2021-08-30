from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
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
    owner = models.ForeignKey(Retailer, on_delete=models.CASCADE, blank=False, null=False, related_name='outlets')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    outlet_type = models.ForeignKey(OutletType, on_delete=models.CASCADE, blank=False, null=False, related_name='outlets')
    location = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    number = models.CharField(max_length=200)
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
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False, null=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=False, null=False)
    bar_code = models.CharField(max_length=13, unique=True, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField( upload_to=user_directory_path, default='products/default.jpg')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

