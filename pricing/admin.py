# admin.py

from django.contrib import admin
from .models import Fruit, DeliveryLocation

admin.site.register(Fruit)
admin.site.register(DeliveryLocation)
