from rest_framework import serializers
from .models import Product, ProductType, Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    price = PriceSerializer()
    product_type = ProductTypeSerializer()

    class Meta:
        model = Product
        fields = '__all__'
