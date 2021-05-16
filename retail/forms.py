from retail.models import User, Retailer
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class RetailerCreateForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_retailer = True
        user.save()
        retailer = Retailer.objects.create(user=user)
        retailer.mobile = self.cleaned_data.get('mobile')
        return user