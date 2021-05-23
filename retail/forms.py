from retail.models import Outlet, User, Retailer
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class RetailerCreateForm(UserCreationForm):
    mobile = forms.CharField()
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_retailer = True
        user.save()
        return user

class OutletForm(forms.ModelForm):
    class Meta:
        model = Outlet
        fields = [
            'owner',
            'name',
            'outlet_type',
            'address',
            'country',
            'county',
            'city',
            'ward',
            'constituency',
            'gps_coordinates',
            'number',
            'amenities',
            'outlet_code',
            'outlet_person',
        ]