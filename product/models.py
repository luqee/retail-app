from django.db import models
from django.utils import timezone

def user_directory_path(instance, filename):
    return 'products/%Y/%m/%d/'.format(instance.id, filename)

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
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True)
    sku = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200)
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
