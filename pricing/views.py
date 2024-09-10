from rest_framework import permissions, generics
from rest_framework.permissions import IsAuthenticated
from .models import Fruit, FruitPrice, DeliveryLocation
from .serializers import FruitSerializer, FruitPriceSerializer, DeliveryLocationSerializer
from rest_framework.throttling import ScopedRateThrottle

class FruitListCreateView(generics.ListCreateAPIView):
    throttle_scope = 'user'
    throttle_classes = [ScopedRateThrottle]
    permission_classes = [IsAuthenticated]
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer


class FruitDetailView(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'user'
    throttle_classes = [ScopedRateThrottle]
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            # Allow unauthenticated access for the retrieve action
            return [permissions.AllowAny()]
        else:
            # Require authentication for update and delete actions
            return [permissions.IsAuthenticated()]
    

class FruitPriceListCreateView(generics.ListCreateAPIView):
    throttle_scope = 'user'
    throttle_classes = [ScopedRateThrottle]
    permission_classes = [IsAuthenticated]
    queryset = Fruit.objects.all()
    queryset = FruitPrice.objects.all()
    serializer_class = FruitPriceSerializer
    

class FruitPriceDetailView(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'user'
    throttle_classes = [ScopedRateThrottle]
    queryset = Fruit.objects.all()
    queryset = FruitPrice.objects.all()
    serializer_class = FruitPriceSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            # Allow unauthenticated access for the retrieve action
            return [permissions.AllowAny()]
        else:
            # Require authentication for update and delete actions
            return [permissions.IsAuthenticated()]
    

class DeliveryLocationListCreateView(generics.ListCreateAPIView):
    throttle_scope = 'user'
    throttle_classes = [ScopedRateThrottle]
    permission_classes = [IsAuthenticated]
    queryset = Fruit.objects.all()
    queryset = DeliveryLocation.objects.all()
    serializer_class = DeliveryLocationSerializer


class DeliveryLocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'user'
    throttle_classes = [ScopedRateThrottle]
    queryset = DeliveryLocation.objects.all()
    serializer_class = DeliveryLocationSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            # Allow unauthenticated access for the retrieve action
            return [permissions.AllowAny()]
        else:
            # Require authentication for update and delete actions
            return [permissions.IsAuthenticated()]
    
