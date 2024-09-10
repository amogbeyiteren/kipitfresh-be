import uuid
from django.db import models

class Fruit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class FruitPrice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    price_per_ton = models.DecimalField(max_digits=10, decimal_places=2)  # Price in thousands

    def __str__(self):
        return f"{self.fruit.name}: {self.price_per_ton} thousand naira per ton"

class DeliveryLocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.CharField(max_length=100, unique=True)
    price_per_delivery = models.DecimalField(max_digits=10, decimal_places=2)  # Price in thousands

    def __str__(self):
        return f"{self.location}: {self.price_per_delivery} thousand naira per delivery"
