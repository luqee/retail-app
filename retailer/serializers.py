from rest_framework import serializers
from retailer.models import Transaction
from retail.models import Brand, OutletType, Product, ProductCategory, User, Retailer, Outlet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields= '__all__'

class RetailerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Retailer
        fields= '__all__'

class OutletTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutletType
        fields= '__all__'

class OutletSerializer(serializers.ModelSerializer):
    outlet_type = OutletTypeSerializer()
    class Meta:
        model = Outlet
        fields= '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields= '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields= '__all__'

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields= '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    outlet = OutletSerializer()
    class Meta:
        model = Transaction
        fields= '__all__'