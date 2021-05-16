from retail.models import User, Retailer
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
        Retailer.objects.create(user=user, mobile=self.cleaned_data.get('mobile'))
        return user