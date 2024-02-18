from rest_framework import serializers
from categories.models import Category
from products.serializers import ProductListSerializer

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'is_active', 'products_count', 'products']