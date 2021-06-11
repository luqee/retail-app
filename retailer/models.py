from django.db import models
from retail.models import Product, Outlet

# Create your models here.

class Transaction(models.Model):
    TYPE_CHOICES = (
        ('in', 'Stock In'),
        ('out', 'Stock Out'),
    )
    quantity=models.IntegerField()
    time=models.DateTimeField(auto_now=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False, related_name='transactions')
    outlet=models.ForeignKey(Outlet, on_delete=models.CASCADE, blank=False, null=False, related_name='transactions')
    tran_type =  models.CharField(max_length=12, choices=TYPE_CHOICES, default='in')

    class Meta:
        ordering = ('-time',)
