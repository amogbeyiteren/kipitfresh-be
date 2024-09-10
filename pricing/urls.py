from django.urls import path
from .views import (
    FruitListCreateView, FruitDetailView,
    FruitPriceListCreateView, FruitPriceDetailView,
    DeliveryLocationListCreateView, DeliveryLocationDetailView
)

urlpatterns = [
    path('fruits/', FruitListCreateView.as_view(), name='fruit-list-create'),
    path('fruits/<int:pk>/', FruitDetailView.as_view(), name='fruit-detail'),
    path('fruit-prices/', FruitPriceListCreateView.as_view(), name='fruit-price-list-create'),
    path('fruit-prices/<int:pk>/', FruitPriceDetailView.as_view(), name='fruit-price-detail'),
    path('delivery-locations/', DeliveryLocationListCreateView.as_view(), name='delivery-location-list-create'),
    path('delivery-locations/<int:pk>/', DeliveryLocationDetailView.as_view(), name='delivery-location-detail'),
]
