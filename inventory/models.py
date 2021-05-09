from django.db import models

class Retailer(models.Model):
    ...

class Outlet(models.Model):
    name = models.CharField(max_length=200)
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



class Product(models.Model):
    ...


class ProductCategory(models.Model):
    ...

class Products(models.Model):
    ...