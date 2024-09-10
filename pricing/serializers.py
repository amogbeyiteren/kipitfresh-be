from rest_framework import serializers
from .models import Fruit, FruitPrice, DeliveryLocation

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ['id', 'name']

class FruitPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FruitPrice
        fields = ['id', 'fruit', 'price_per_ton']

class DeliveryLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryLocation
        fields = ['id', 'location', 'price_per_delivery']
