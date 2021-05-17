from rest_framework import serializers
from retailer.models import Transaction
from retail.models import User, Retailer, Outlet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields= '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields= '__all__'

class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields= '__all__'

class OutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields= '__all__'