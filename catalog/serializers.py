from rest_framework import serializers

from catalog.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializing Product model
    """
    class Meta:
        model = Product
        fields = ('id', 'sku', 'name', 'price', 'brand',)
