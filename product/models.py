from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


def user_directory_path(instance, filename):
    return 'products/%Y/%m/%d/'.format(instance.id, filename)


class Brand(models.Model):
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ('brand_name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.brand_name




class ProductCategory(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
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





