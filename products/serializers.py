from rest_framework import serializers

from products.models import Product, Sku


class ProductListSerializer(serializers.ModelSerializer):
    """
    To show list of products.
    """

    class Meta:
        model = Product
        fields = ["name", "ingredients"]


class SkuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sku
        fields = ['id', 'product', 'size', 'measurement_unit', 'cost_price', 'status', 'platform_commission']
        read_only_fields = ['id', 'selling_price', 'markup_percentage']
        

    
    def create(self, validated_data):
        validated_data['status'] = 0  # Set the default status for a new Sku
        return super().create(validated_data)


class SkuEditStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sku
        fields = ['status']

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance